empty_tuple = ()
another_tuple = tuple()
print(id(empty_tuple))
print(id(another_tuple))

empty_list = []
another_list = list()
print(id(empty_list))
print(id(another_list))

my_tuple = ("python", "java", "kotlin")
print(my_tuple)
my_tuple = "python", "java", "kotlin"
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
print(type(my_tuple))
print(len(my_tuple))

a = my_tuple[0]
b = my_tuple[1]
c = my_tuple[2]
print(a, b, c)

a, b, c = my_tuple
print(a, b, c)

my_tuple = (1, 2, 3, 4, 5)
a, b, c, *rest = my_tuple
print(a, b, c)
print(type(rest))
rest.append(6)
print(rest)
a, b, c, *_ = my_tuple
print(a, b, c)
print(_) # Ignoring value
a, *_, e = my_tuple
print(a, e)
print(_) # Ignoring value

a = 100
b = 200
print(a, b)
# temp = a
# a = b
# b = temp
a, b = b, a
print(a, b)

my_list = [1, 2, 3, 4, 5]
some_tuple = tuple(my_list)
print(some_tuple)
for el in some_tuple:
    print(el)
print(some_tuple[0])

for i in range(len(some_tuple)):
    print(i, some_tuple[i])
