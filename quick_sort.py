def get_pivot(table):
    if len(table) % 2 == 0:
        return table[int(len(table)/2) - 1]
    return table[int((len(table) - 1)/2)]


def quick_sort(lst):
    stack = []
    stack.append(lst[:])
    lst.clear()
    stack_depth = 1
    while stack:
        stack_depth = max(stack_depth, len(stack))
        current_list = stack.pop()
        if len(current_list) <= 1:
            lst += current_list
            continue
        left_elements = []
        right_elements = []
        pivot = get_pivot(current_list)
        current_list.remove(pivot)
        for elem in current_list:
            if elem < pivot:
                left_elements.append(elem)
            else:
                right_elements.append(elem)
        stack.append(right_elements[:])
        stack.append(left_elements[:] + [pivot])
    return lst, stack_depth
