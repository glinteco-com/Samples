list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_list = []

for num in list1:
    if num in list2:
        common_list.append(num)

print("Common elements:", common_list)
