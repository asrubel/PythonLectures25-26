from random import shuffle

my_list = list(range(10))
shuffle(my_list)
print(my_list)

print(my_list[0])
print(my_list[len(my_list) - 1])
print(my_list[-1])
print(my_list[-2])
print(my_list[-len(my_list)])

print(my_list[-3])
print(my_list[-4])

print(my_list)
print(my_list[2:7])
print(my_list[2:9:2])

print(my_list[:7])
print(my_list[4:])

second_list = my_list
copy_of_list = my_list[:]
print(id(my_list))
print(id(second_list))
print(id(copy_of_list))

print(my_list[::3])
print(my_list[::-1])
print(my_list[9:3:-2])

my_str = "Python"
print(my_str)
print(my_str[::-1])
print(my_str[2:5])
print(my_str[4:1:-1])
