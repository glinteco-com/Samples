num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_even = 0

for num in num_list:
    if num % 2 == 0:
        sum_even += num

print("The sum of all the even numbers in the list is:", sum_even)
