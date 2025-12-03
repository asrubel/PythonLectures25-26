# __next__()
# __iter__()

my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)
print(my_iterator)
print(type(my_iterator))

for item in my_list:
    print(item)

for item in iter(my_list):
    print(item)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
for item in my_iterator:
    print(item)

first_names = ["Oleksandr", "Hanna", "Ivan"]
last_names = ["Petrenko", "Zubenko", "Shevchenko", "Romanenko"]

for i in range(min(len(first_names), len(last_names))):
    print(first_names[i], last_names[i])

for first, last in zip(first_names, last_names):
    print(first, last)
print(type(zip(first_names, last_names)))

n = 1
for last in last_names:
    print(n, last)
    n += 1

for num, last in enumerate(last_names, start=1):
    print(num, last)
print(type(enumerate(last_names, start=1)))
