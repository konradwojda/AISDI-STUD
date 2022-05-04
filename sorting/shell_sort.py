from insertion_sort import insertion_sort


def make_gaps(_list):
    gaps = []
    gap = 1
    while gap < len(_list):
        gaps.append(gap)
        gap *= 3
        gap += 1
    if len(gaps) == 1:
        return [1]
    else:
        return reversed(gaps[:-1])


def shell_sort(_list, gaps=None):
    if not gaps:
        gaps = make_gaps(_list)
    for gap in gaps:
        for i in range(gap):
            _list[i::gap] = insertion_sort(_list[i::gap])
    return _list
