from insertion_sort import insertion_sort


def test_instertion_sort_case1():
    list = [4, 3, 5, 2, 1]
    assert insertion_sort(list) == [1, 2, 3, 4, 5]


def test_instertion_sort_case2():
    list = [1, 2, 3, 4, 5]
    assert insertion_sort(list) == [1, 2, 3, 4, 5]


def test_instertion_sort_case3():
    list = [3, 1, 2, 1, 1, 2, 2, 2, 2]
    assert insertion_sort(list) == [1, 1, 1, 2, 2, 2, 2, 2, 3]