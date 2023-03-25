string = "Hello, World!"
vowels = "aeiouAEIOU"
count = 0

for letter in string:
    if letter in vowels:
        count += 1

print("The number of vowels in the string is:", count)
