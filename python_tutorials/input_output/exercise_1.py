name = input("What is your name? ")
age = input("What is your age? ")
with open("personal_info.txt", "w") as f:
    f.write(f"Name: {name}\nAge: {age}")
