empty_set = set()
print(type(empty_set))

my_set = {1, 2, 3, 4, 4, 4, 4, 4, 5}
print(my_set)

letters = set("pythoooooooonnnn")
print(letters)

set_1 = {'A', 'B', 'C'}
set_2 = {'C', 'A', 'B'}
print(set_1 == set_2)

print(len(set_1))
print('A' in set_1)
print('D' in set_1)
print('D' not in set_1)

for i in set_1:
    print(i)

set_1.remove('A')
print(set_1)
set_1.discard('A')
print(set_1)
set_1.add('D')
print(set_1)
