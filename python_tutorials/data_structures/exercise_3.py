def common_elements(list1, list2):
    common = []
    for num in list1:
        if num in list2 and num not in common:
            common.append(num)
    return common


# Example usage
my_list1 = [1, 2, 3, 4, 5]
my_list2 = [3, 4, 5, 6, 7]
print(common_elements(my_list1, my_list2))  # Output: [3, 4, 5]
