def quicksort(table):
    if len(table) < 2:
        return table
    left_elements = []
    right_elements = []
    pivot = get_pivot(table)
    table.remove(pivot)
    for element in table:
        if element < pivot:
            left_elements.append(element)
        else:
            right_elements.append(element)
    left_elements = quicksort(left_elements)
    right_elements = quicksort(right_elements)
    table.clear()
    table += left_elements + [pivot] + right_elements
    return table


def get_pivot(table):
    if len(table) % 2 == 0:
        return table[int(len(table)/2) - 1]
    return table[int((len(table) - 1)/2)]
