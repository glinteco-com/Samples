str_list = ["cat", "dog", "elephant", "lion", "tiger"]

longest_str = ""

for string in str_list:
    if len(string) > len(longest_str):
        longest_str = string

print("The longest string in the list is:", longest_str)
