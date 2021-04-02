def quicksort(table, counter=-1, deepest_recursion=0):
    counter += 1
    deepest_recursion = max(counter, deepest_recursion)
    if len(table) < 2:
        counter -= 1
        return table, counter, deepest_recursion
    left_elements = []
    right_elements = []
    pivot = get_pivot(table)
    table.remove(pivot)
    for element in table:
        if element < pivot:
            left_elements.append(element)
        else:
            right_elements.append(element)
    left_elements, counter, deepest_recursion = quicksort(
        left_elements,
        counter,
        deepest_recursion
        )
    right_elements, counter, deepest_recursion = quicksort(
        right_elements,
        counter,
        deepest_recursion
        )
    table.clear()
    table += left_elements + [pivot] + right_elements
    counter -= 1
    return table, counter, deepest_recursion


def get_pivot(table):
    if len(table) % 2 == 0:
        return table[int(len(table)/2) - 1]
    return table[int((len(table) - 1)/2)]
