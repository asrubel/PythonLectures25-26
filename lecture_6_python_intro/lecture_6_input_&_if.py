user_input = input("Enter the number: ")
print(user_input)
print(type(user_input))
print(id(user_input))

user_num = int(user_input)
print(user_num)
print(type(user_num))
print(id(user_num))

user_num = user_num + 1000
print(user_num)
print(type(user_num))
print(id(user_num))

if user_num % 2 == 0:
    print("No remaining")
else:
    print("Has remaining")
