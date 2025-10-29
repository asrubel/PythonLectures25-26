def multiply(first, second, *args):
    print(args)
    print(type(args))

    res = first * second
    for arg in args:
        # res = res * arg
        res *= arg

    return res


print(multiply(3, 4))
print(multiply(3, 4, 7, 7, 8))
print(multiply(3, 4, 7, 7, 8, 19, 3))
print(multiply(3, 4, *range(1, 100)))

print(range(1, 100))
print(*range(1, 100))
