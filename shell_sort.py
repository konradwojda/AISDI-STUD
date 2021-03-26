from insertion_sort import insertion_sort


def make_gaps(_list):
    gaps = []
    list_len = len(_list)
    while list_len != 1:
        list_len //= 2
        gaps.append(list_len)
    return gaps


def shell_sort(_list, gaps=None):
    if not gaps:
        gaps = make_gaps(_list)
    for gap in gaps:
        for i in range(gap):
            _list[i::gap] = insertion_sort(_list[i::gap])
    return _list
