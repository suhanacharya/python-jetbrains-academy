# put your python code here

# key, values = test_dict.keys(), test_dict_values()

# print("min: " + str(min(test_dict.values())))
# print("max: " + str(min(test_dict.values())))

# test_dict = {"a": 43, "d": 1233, "c": 8, "b": 1}

x = {v: k for k, v in test_dict.items()}

print("min: " + str(x[min(x.keys())]))
print("min: " + str(x[max(x.keys())]))
