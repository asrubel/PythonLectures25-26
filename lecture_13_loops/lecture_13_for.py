# Iterable
my_list = [1, 2, 3, 4, 5]
my_str = "Python"
my_tuple = (1, 2, 3, 4, 5)

for i in my_list:
    print(i)

for i in my_tuple:
    print(i)

for i in my_str:
    print(i)

my_set = {1, 2, 3, 4, 5}
for i in my_set:
    print(i)

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
for key in my_dict:
    print(key)
for val in my_dict.values():
    print(val)
for pair in my_dict.items():
    print(pair)
for k, v in my_dict.items():
    print(k, v)
