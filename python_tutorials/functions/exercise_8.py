def find_index(lst, n):
    if n in lst:
        return lst.index(n)
    else:
        return -1


print(find_index([1, 2, 3, 4, 5], 3))  # output: 2
