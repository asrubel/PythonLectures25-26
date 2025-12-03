def multi_number(a, n):
    result = []
    i = 1
    while i <= n:
        result.append(a * i)
        i += 1
    return result


def multi_generator(a, n):
    i = 1
    while i <= n:
        yield a * i
        i += 1


print(multi_number(5, 10))
my_generator = multi_generator(5, 10)
print(my_generator)
print(type(my_generator))

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
for el in my_generator:
    print(el)

# print(next(my_generator))
