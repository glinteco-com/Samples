numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_of_odds = 0

for number in numbers:
    if number % 2 == 1:
        sum_of_odds += number

print("The sum of the odd numbers in the list is:", sum_of_odds)
