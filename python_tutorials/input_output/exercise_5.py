with open("names.txt", "r") as f:
    names = f.read().splitlines()
    reversed_names = ", ".join(names[::-1])
    print(reversed_names)
