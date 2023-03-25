string = input("Enter a string: ")

vowel_count = 0

for char in string:
    if char in "aeiouAEIOU":
        vowel_count += 1

print("Number of vowels:", vowel_count)
