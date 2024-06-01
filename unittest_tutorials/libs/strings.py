def count_e_letters(name: str) -> int:
    count = 0

    if not name:
        return count

    for letter in name:
        if letter == 'e':
            count += 1

    return count


def count_vowels(a_string: str) -> int:
    count = 0

    if not name:
        return count

    vowels = "aeiouAEIOU"
    for char in a_string:
        if char in vowels:
            count += 1
    return count
