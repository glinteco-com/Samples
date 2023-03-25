with open("numbers.txt", "r") as f:
    numbers = [int(line.strip()) for line in f]
    print(sum(numbers))
