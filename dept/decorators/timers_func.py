import timeit
import time


def timer(func):
    def wrapper():
        run_time = timeit.timeit(func, number=1)
        print(f'Runtime: {run_time}')
    return wrapper()


def runtime(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_total = time.time() - time_start
        print(f'Runtime: {time_total}')
        return result
    return wrapper()
