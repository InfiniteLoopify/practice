from timeit import timeit
from operator import itemgetter
from itertools import chain


def do_stuff(i):
    return i + 1


def for_loop(num):
    x = [i for i in range(num)]
    for i in x:
        do_stuff(i)
        do_stuff(i)
        do_stuff(i)


def for_loop_gen(num):
    x = (i for i in range(num))
    for i in x:
        do_stuff(i)
        do_stuff(i)
        do_stuff(i)


def for_loop_range(num):
    for i in range(num):
        do_stuff(i)
        do_stuff(i)
        do_stuff(i)


def list_comp(num):
    (do_stuff(i) for i in range(num))
    (do_stuff(i) for i in range(num))
    (do_stuff(i) for i in range(num))


def list_comp_arr(num):
    [do_stuff(i) for i in range(num)]
    [do_stuff(i) for i in range(num)]
    [do_stuff(i) for i in range(num)]


def map_loop(num):
    map(do_stuff, range(num))
    map(do_stuff, range(num))
    map(do_stuff, range(num))


def filter_iter(num):
    filter(lambda x: x % 2 == 0, range(num))


def filter_list_comp(num):
    (i for i in range(num) if i % 2 == 0)


def filter_list_comp_arr(num):
    [i for i in range(num) if i % 2 == 0]


def sort_lambda(num):
    sorted(zip(range(num), range(num)), key=lambda x: x[1], reverse=True)


def sort_itemgetter(num):
    sorted(zip(range(num), range(num)), key=itemgetter(1), reverse=True)


def concat_plus(num):
    x = []
    x += (i for i in range(num * 5))


def concat_chain(num):
    x = []
    x = chain(x, (i for i in range(num * 5)))


def string_plus(num):
    x = ("qwerty" for i in range(num * 5))
    q = ""
    for i in x:
        q += i


def string_join(num):
    x = ("qwerty" for i in range(num * 5))
    q = "".join(x)


def main():
    funcs = [
        # for_loop,
        # for_loop_gen,
        # for_loop_range,
        # list_comp,
        # list_comp_arr,
        # map_loop,
        # filter_iter,
        # filter_list_comp,
        # filter_list_comp_arr,
        # sort_lambda,
        # sort_itemgetter,
        # concat_plus,
        # concat_chain,
        string_plus,
        string_join,
    ]

    vals = [timeit(lambda: func(1000000), number=10) for func in funcs]
    max_val = max(vals)

    for val, func in zip(vals, funcs):
        print(func.__name__, val / max_val * 100)


if __name__ == "__main__":
    main()
