num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = []

for num in num_list:
    if num % 2 == 0:
        even_list.append(num)

print("Even numbers:", even_list)
