num_list = [1, 2, 3, 4, 5]

product = 1
i = 0

while i < len(num_list):
    product *= num_list[i]
    i += 1

print("The product of all the numbers in the list is:", product)
