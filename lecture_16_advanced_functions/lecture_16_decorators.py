import time

def out_decorator(some_fun):
    def wrapper(args_for_some_fun):
        print(type(some_fun))
        print(type(args_for_some_fun))
        print(args_for_some_fun)

        if args_for_some_fun == "Java":
            return "Python!!!!! NOT Java"
        else:
            print("Before...")
            result = some_fun(args_for_some_fun)
            print("After...")
            return result

    return wrapper


@out_decorator
def my_fun(name):
    print(f"Hello, {name}")


my_fun("Oleksii")
my_fun("Java")


def timer_decorator(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(start)
        fun(*args, **kwargs)
        end = time.time()
        print(end)
        print(f"Finished in {end - start:.5f} seconds")

    return wrapper


@timer_decorator
@out_decorator
def huge_calculations(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


huge_calculations(1000)
