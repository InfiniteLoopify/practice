def func():
    # for i in range(5):
    #     yield i
    yield from range(5)


if __name__ == "__main__":
    x = func()
    for i in range(6):
        try:
            print(next(x))
        except StopIteration:
            print("end---")
            break
