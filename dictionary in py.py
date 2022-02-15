from PyDictionary import PyDictionary

dictionary = PyDictionary()
dict_obj = dictionary.meaning("friendship")

for ty, val in zip(dict_obj, dict_obj.values()):
    print(f"as {ty}:\n{val}")
