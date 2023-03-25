def sum_even(numbers):
    result = 0
    for num in numbers:
        if num % 2 == 0:
            result += num
    return result


# Example usage
my_list = [1, 2, 3, 4, 5, 6]
print(sum_even(my_list))  # Output: 12
