dict1 = {1: "apple", 2: 5, 3: "banana", 4: "orange"}

new_dict = {}

for key, value in dict1.items():
    if type(value) == str:
        new_dict[key] = value

print("New dictionary:", new_dict)
