empty_dict = dict()
print(type(empty_dict))

my_dict = {"518": 10, "516": 20, "519st": 10, "516st": 10, "518st": 5}
print(my_dict["518"])
my_dict["518"] = my_dict["518"] + 1
print(my_dict)

print("Keys only -------------------")
for key in my_dict:
    print(key)

print(my_dict.keys())
for key in my_dict.keys():
    print(key)

print("Values only -----------------")
for value in my_dict.values():
    print(value)

print("Items only ------------------")
print(my_dict.items())
for pair in my_dict.items():
    print(pair)

for key, value in my_dict.items():
    print(key, " -> ", value)

new_dict = {1: "python", 3.2: "float", "str": 100,
            (): [], (1, 2, 3): "KhAI"}
print(new_dict)
print(hash((1, 2, 3, 4)))
