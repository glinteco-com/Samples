def longest_word(lst):
    return max(lst, key=len)


print(longest_word(["apple", "banana", "pear", "grape"]))  # output: "banana"
