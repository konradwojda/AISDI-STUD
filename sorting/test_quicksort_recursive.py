from quicksort_recursive import quicksort, get_pivot


def test_get_pivot_case1():
    table = [4, 3, 5, 2, 1]
    assert get_pivot(table) == 5


def test_get_pivot_case2():
    table = [4, 3, 5, 2, 1, 4, 6, 9]
    assert get_pivot(table) == 2


def test_get_pivot_case3():
    table = [4, 2]
    assert get_pivot(table) == 4


def test_quicksort_case1():
    table = [4, 3, 5, 2, 1]
    assert quicksort(table) == [1, 2, 3, 4, 5]


def test_quicksort_case2():
    table = [1, 2, 3, 4, 5]
    assert quicksort(table) == [1, 2, 3, 4, 5]


def test_quicksort_case3():
    table = [3, 1, 2, 1, 1, 2, 2, 2, 2]
    assert quicksort(table) == [1, 1, 1, 2, 2, 2, 2, 2, 3]


def test_in_place():
    a = [3, 2, 1]
    quicksort(a)
    assert a == [1, 2, 3]
