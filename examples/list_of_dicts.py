lst = [{'a': 'aa', 'b': 2}, {'a': 'bb', 'b': 2}, {'a': 'cc', 'b': 3}, {'a': 'dd', 'b': 4}]

# print(lst[0])
# print(lst[0]['a'])
# print(lst['a'])

# python search in list of dictionaries

# The simple way
dict_i_want = None

for d in lst:
    if d["a"] == "aa":
        dict_i_want = d

if dict_i_want is not None:
    print(dict_i_want['b'])
    dict_i_want['b'] = 9
else:
    print("no matches - :(")
print(lst)
# print(dict_i_want)

# index_of_dict_i_want = lst.index(dict_i_want)
# print(index_of_dict_i_want)
# print(lst[index_of_dict_i_want])

# The better way
# dict_i_want = next((d for d in lst if d["a"] == "bb"), None)
# index_i_want = next((i for i, d in enumerate(lst) if d["a"] == "bb"), -1)
# print(dict_i_want, index_i_want)

# The Pythonic way
# dict_i_want = list(filter(lambda d: d["a"] == "bb", lst))[0]
# print(dict_i_want)
