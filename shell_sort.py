from insertion_sort import insertion_sort


def shell_sort(_list, gaps):
    for gap in gaps:
        for i in range(gap):
            _list[i::gap] = insertion_sort(_list[i::gap])
    return _list
