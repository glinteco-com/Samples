with open("inventory.txt", "r") as f:
    inventory = {}
    for line in f:
        name, price = line.strip().split(",")
        inventory[name] = float(price)
    max_price = max(inventory.values())
    for name, price in inventory.items():
        if price == max_price:
            print(f"{name}: {price}")
