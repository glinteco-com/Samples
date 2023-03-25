string_list = ["apple", "banana", "pear", "grape", "orange"]

count = 0

for string in string_list:
    if "a" in string:
        count += 1

print("Number of strings containing 'a':", count)
