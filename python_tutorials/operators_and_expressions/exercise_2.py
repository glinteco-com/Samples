num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = 0

for num in num_list:
    if num % 2 == 0:
        even_sum += num

print("Sum of even numbers:", even_sum)
