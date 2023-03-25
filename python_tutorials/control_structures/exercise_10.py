def calculate_total(dictionary):
    total = 0
    for _, price in dictionary.items():
        total += price
    return total


items = {"apple": 0.5, "banana": 0.25, "pear": 0.75}
total = calculate_total(items)
print("Total cost: $", total)
