print('Python 3.11')
print("Python 3.11")

print('Python "3.11"')
print("Python '3.11'")

print('Python \'3.11\'')
print("Python \"3.11\"")

# TODO - Implement this (reminder)

my_num = 100
print(id(my_num))
print(type(my_num))
my_num += 10
print(id(my_num))
print(my_num.bit_count())

my_string = "Python, version '3.11'"
print(my_string)
print(id(my_string))
new_string = my_string.replace('1', '2')
print(new_string)
print(id(new_string))

print(my_string.lower())
print(my_string.upper())
print(my_string.capitalize())
print(my_string.title())
print(my_string.swapcase())

redundant_str = "   fdgdfg   "
print(redundant_str)
print(redundant_str.lstrip())
print(redundant_str.rstrip())
print(redundant_str.strip())

redundant_str = "Mississippi"
print(redundant_str)
print(redundant_str.lstrip('ips'))
print(redundant_str.rstrip('ips'))
print(redundant_str.strip('Mis'))

some_str = "pythonyth"
print(some_str.find('th'))
print(some_str.find('th', 5))
print(some_str.index('y'))
print(some_str.count('y'))
print(some_str.count('yth'))

user_input = input("Enter a string: ")
print(user_input)
print(user_input.split())
