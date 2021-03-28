from shell_sort import shell_sort


def test_shell_sort1():
    _list = [3, 8, 4, 5, 2, 6, 1, 7, 9]
    gaps = [5, 3, 2, 1]
    assert shell_sort(_list, gaps) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_shell_sort2():
    _list = [3, 8, 4, 5, 2, 6, 1, 7, 9]
    assert shell_sort(_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_in_place():
    _list = [3, 2, 1]
    shell_sort(_list)
    assert _list == [1, 2, 3]
