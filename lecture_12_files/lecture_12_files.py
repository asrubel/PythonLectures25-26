from time import sleep

file = open("groups.txt", "r")
# print(file.read())
print(type(file))

print(file.readline(5))
print(file.readline(5))
print(file.readline(5))
print(file.readline(5))
print(file.readline(5))
print(file.readline(5))
file.close()

file = open("groups.txt", "r")
lines = file.readlines()
print(lines)
for line in lines:
    print(line)
file.close()

my_list = ["Java", "Kotlin", "Python", "JavaScript"]
my_file = open("my_text.txt", "w+", encoding="utf-8")
for lang in my_list:
    my_file.write(f"{lang}\n")
    print(lang)
print(my_file.readlines())
my_file.close()

my_file = open("my_text.txt", "a+", encoding="utf-8")
my_file.write("\n")
my_file.write("KhAI\n")
my_file.write("D://CT\n")
print(my_file.readlines())

my_file.writelines(lines)
my_file.close()

my_file = open("my_text.txt", "r", encoding="utf-8")
print(my_file.readlines())
my_file.close()
