def average(numbers):
    if len(numbers) == 0:
        raise ValueError("List is empty")
    else:
        return sum(numbers) / len(numbers)
