print(range(10))
print(type(range(10)))
print(list(range(10)))

for i in range(10):
    print(i)

# for i in range(1_000_000):
#     print(i)

for i in range(5, 45, 10):
    print(i)

for _ in range(10):
    print("Python")

for i in range(1, 6):
    for j in range(1, 6):
        print(i, j, i * j)

for i in range(10):
    if i == 7:
        break
    if i % 2 == 0:
        print("Even")
    else:
        print(i)
    if i % 2 == 1:
        print("Odd")
        continue
