strings = ["Python", "Java", "C", "Ruby", "Perl", "JavaScript"]

shortest = strings[0]

for string in strings:
    if len(string) < len(shortest):
        shortest = string

print("The shortest string is:", shortest)
