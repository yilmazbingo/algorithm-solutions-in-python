def timed(fn):
    from time import perf_counter
    from functools import wraps
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ["{0}={1}".format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ",".join(all_args)
        print("{0} ({1}) took {2:.6f} to run.".format(fn.__name__, args_str, elapsed))
        return result

    return inner


# wirte n finonaci number function
@timed
def recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)

@timed
def calculate_recursive(n):
    return recursive_fib(n)
calculate_recursive(3)
#recursive_fib(3)

def loop_fib(n):
    fib_1=1
    fib_2=1
    for i in range(3,n+1):
        fib_1,fib_2=fib_2,fib_1+fib_2
    return fib_2