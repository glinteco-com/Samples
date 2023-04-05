# Write a test for a function that sorts a list of integers in ascending order.

def sort(a_list):
    return sorted(a_list)


def test_sorting():
    assert sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
