def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join([c for c in s if c not in vowels])


print(remove_vowels("hello world"))  # output: "hll wrld"
