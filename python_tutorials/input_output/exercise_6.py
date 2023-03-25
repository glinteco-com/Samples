filename = input("Enter a filename: ")
with open(filename, "r") as f:
    words = f.read().split()
    print(len(words))
