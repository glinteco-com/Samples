def palindromes(strings):
    result = []
    for string in strings:
        if string == string[::-1]:
            result.append(string)
    return result


# Example usage
my_list = ["racecar", "hello", "level", "world"]
print(palindromes(my_list))  # Output: ['racecar', 'level']
