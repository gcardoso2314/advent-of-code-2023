import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Function {func.__name__} took {time.time() - start:.4f}s")
        return res

    return wrapper
