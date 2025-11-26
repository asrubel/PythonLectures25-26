num = 1
while num <= 10:
    print(num)
    num += 1

# print(num)

while True:
    user_input = input("Enter a command: ")
    if user_input.lower() in {"quit", "exit", "q"}:
        break

val = 0
while val < 10:
    val += 1
    if val % 2 == 0:
        continue
    else:
        print(val)
