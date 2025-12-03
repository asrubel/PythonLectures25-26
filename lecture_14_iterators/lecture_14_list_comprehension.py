my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)

gen_list = [i for i in range(1, 11)]
print(gen_list)

res_list = []
for i in gen_list:
    res_list.append(i ** 2)
print(res_list)

gen_list = [i ** 2 for i in range(1, 11)]
print(gen_list)

filtered_list = [i for i in range(1, 11) if i % 2 == 0]
print(filtered_list)

gen_obj = (i for i in range(1, 11))
print(gen_obj)
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
for i in gen_obj:
    print(i)

# print(next(gen_obj))
