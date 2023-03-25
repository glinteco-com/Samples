def reverse_string(input_str):
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    else:
        return input_str[::-1]
