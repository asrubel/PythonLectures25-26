with open("my_text.txt", "a") as my_file:
    my_file.write("Python!!!!")

print("The end")

n = 1_000
files = []

for _ in range(n):
    with open("my_text.txt", "r") as f:
        files.append(f.read())

print(files)

with open("groups.txt", "r") as input_file, \
    open("courses.txt", "w") as output_file:
    for line in input_file:
        output_file.write(line)
