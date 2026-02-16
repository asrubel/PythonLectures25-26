"""Modules"""
# print("Modules")


def my_fun(a, b):
    return a + b


x = 100


class MyClass:
    pass


# print(__name__)
# print(x)
# print(type(MyClass))
# print(my_fun(x, 2))

if __name__ == '__main__':
    print(__name__)
    print(x)
    print(type(MyClass))
    print(my_fun(x, 2))
