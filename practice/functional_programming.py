import itertools
import functools
import operator
import time
from timeit import timeit


def itertools_run():
    ac = itertools.accumulate([1, 2, 3, 4, 5], operator.mul)
    print(itertools.accumulate.__name__, list(ac))

    ch = itertools.chain([1, 2, 3], [4, 5, 6])
    print(itertools.chain.__name__, list(ch))

    co = itertools.combinations("abcd", 2)
    print(itertools.combinations.__name__, list(co))

    co = itertools.combinations_with_replacement("abcd", 2)
    print(itertools.combinations_with_replacement.__name__, list(co))

    pr = itertools.permutations("abcd", 2)
    print(itertools.permutations.__name__, list(pr))

    bh = itertools.batched([1, 2, 3, 4, 5, 6, 7, 8], 3)
    print(itertools.batched.__name__, list(bh))

    cm = itertools.compress("abcd", [1, 0, 1, 1])
    print(itertools.compress.__name__, list(cm))

    cn = itertools.count(3.5, 0.5)
    print(itertools.count.__name__, list(next(cn) for i in range(10)))

    grp = itertools.groupby("AAAABBBCCDAABBB")
    print(itertools.groupby.__name__, [list(g) for k, g in grp])

    pr = itertools.product("abc", repeat=2)
    print(itertools.product.__name__, list(pr))

    mul = map(operator.mul, range(5), range(5))
    print(map.__name__, list(mul))


def functools_run():
    print(functools.reduce.__name__, functools.reduce(operator.add, range(10)))


@functools.lru_cache
def deterministic_func(a: int, b: tuple[str, float]) -> str:
    time.sleep(3)
    return "".join((str(a), b[0], str(b[1])))


def deterministic_run():
    for i in range(5):
        x = timeit(lambda: deterministic_func(i, ("a", float(i))))
        print("before_cache", x)
        x = timeit(lambda: deterministic_func(i, ("a", float(i))))
        print("after_cache", x)


def partial_run():
    part = functools.partial(deterministic_func, b=("b", 2.0))
    part(1)
    print("partial params:", part.keywords)


def my_decorator(*args, **kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs_inner):
            print(kwargs.get("before"))
            ret_val = func(**kwargs_inner)
            print(kwargs.get("after"))
            return ret_val

        return wrapper

    return decorator


@my_decorator(before="before", after="after")
def decorator_run():
    print(deterministic_func(1, ("a", float(1))))


if __name__ == "__main__":
    # itertools_run()
    # functools_run()
    # deterministic_run()
    # partial_run()
    decorator_run()
