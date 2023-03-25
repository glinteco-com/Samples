def find_sum_pair(lst, target_sum):
    seen = set()
    for num in lst:
        complement = target_sum - num
        if complement in seen:
            return (num, complement)
        seen.add(num)
    return None
