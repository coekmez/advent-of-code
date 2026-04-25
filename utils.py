from datetime import datetime


def timeit(func):
    t_0 = datetime.now().microsecond

    def inner(x):
        return func(x)

    print(f"Execution time: {(datetime.now().microsecond - t_0)} ms")

    return inner
