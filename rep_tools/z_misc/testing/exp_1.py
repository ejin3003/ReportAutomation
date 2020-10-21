
test_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}
test_dict.update({"d": 4})
test_dict.clear()

print(test_dict.keys())
print(test_dict.values())
print(test_dict.items())

print(test_dict["a"])
print(test_dict.get("a"))


test = {key: value*2 for (key, value) in test_dict.items()}
print(print(test))
