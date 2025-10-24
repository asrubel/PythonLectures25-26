my_list = ["Python", "Java", "Kotlin", "C#", "C++"]
print(my_list)
print(id(my_list))

print(", ".join(my_list))
my_list.append("Swift")
my_list.append("Rust")
my_list.append("Dart")
print(my_list)
print(id(my_list))

my_list.extend(["C", "Pascal", "Haskell"])
print(my_list)
print(id(my_list))

my_list.remove("Pascal")
print(my_list)
del my_list[1]
print(my_list)

for element in my_list:
    print(element)

for symbol in "Python":
    print(symbol)

for i in range(10):
    print(i)

for i in range(5):
    print(str(i) + ' ' + my_list.pop())

print(my_list)
print(my_list.pop(0))
print(my_list.pop(1))
print(my_list)

that_list = my_list
my_list.append("Python")
print(that_list)
print(len(that_list))
print(len(my_list[0]))

letters_list = list("Python")
print(letters_list)
print(len(letters_list))
