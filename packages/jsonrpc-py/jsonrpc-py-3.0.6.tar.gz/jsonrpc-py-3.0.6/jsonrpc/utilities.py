from asyncio import AbstractEventLoop, Future, Task, TaskGroup, get_running_loop
from collections.abc import Callable, Coroutine, Generator, Iterable, Iterator, MutableMapping
from contextvars import Context, copy_context
from functools import partial
from inspect import iscoroutinefunction
from typing import Any, Final, Literal, ParamSpec, TypeAlias, TypeGuard, TypeVar, final

__all__: Final[tuple[str, ...]] = (
    "ensure_async",
    "is_iterable",
    "make_hashable",
    "multiple_coroutines",
    "Undefined",
    "UndefinedType",
)

T = TypeVar("T")
P = ParamSpec("P")
CoroutineLike: TypeAlias = Generator[Any, None, T] | Coroutine[Any, Any, T]


def ensure_async(user_function: Callable[P, Any], /, *args: P.args, **kwargs: P.kwargs) -> Future[Any]:
    loop: AbstractEventLoop = get_running_loop()
    context: Context = copy_context()

    if iscoroutinefunction(callback := partial(user_function, *args, **kwargs)):
        return loop.create_task(callback(), context=context)
    else:
        return loop.run_in_executor(None, context.run, callback)


def is_iterable(obj: Any, /) -> TypeGuard[Iterable[Any]]:
    try:
        iter(obj)
    except TypeError:
        return False
    else:
        return True


def make_hashable(obj: Any, /) -> Any:
    if isinstance(obj, MutableMapping):
        return tuple((key, make_hashable(value)) for key, value in sorted(obj.items()))
    #: ---
    #: Try hash to avoid converting a hashable iterable (e.g. string, frozenset)
    #: to a tuple:
    try:
        hash(obj)
    except TypeError:
        if is_iterable(obj):
            return tuple(map(make_hashable, obj))
        #: ---
        #: Non-hashable, non-iterable:
        raise

    return obj


async def multiple_coroutines(coroutines: Iterable[CoroutineLike[T]], /) -> list[T]:
    def exception_from_group(exc: BaseException) -> Iterator[BaseException]:
        if isinstance(exc_group := exc, BaseExceptionGroup):
            for nested in exc_group.exceptions:
                yield from exception_from_group(nested)
        else:
            yield exc

    def populate_results(task: Task[T]) -> None:
        if not task.cancelled() and task.exception() is None:
            result: Final[T] = task.result()
            results.append(result)

    context: Context = copy_context()
    results: list[T] = []
    try:
        async with TaskGroup() as tg:
            for _, coroutine in enumerate(coroutines):
                task: Task[T] = tg.create_task(coroutine, context=context)
                task.add_done_callback(populate_results, context=context)
    except BaseExceptionGroup as exc_group:
        #: ---
        #: Propagate the first raised exception from exception group:
        exc, *_ = exception_from_group(exc_group)
        raise exc from None

    return results


@final
class UndefinedType:
    __slots__: tuple[str, ...] = ()

    def __repr__(self) -> Literal["Undefined"]:
        return "Undefined"

    def __hash__(self) -> Literal[0xBAADF00D]:
        return 0xBAADF00D

    def __eq__(self, obj: Any) -> bool:
        return isinstance(obj, self.__class__)

    def __bool__(self) -> Literal[False]:
        return False


Undefined: Final[UndefinedType] = UndefinedType()
