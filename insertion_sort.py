def swap_elements(list, id1, id2):
    temp = list[id1], list[id2]
    list[id2], list[id1] = temp
    return list


def insertion_sort(list):
    for marker in range(1, len(list)):
        for element in range(marker, 0, -1):
            if list[element] < list[element-1]:
                list = swap_elements(list, element, element-1)
            else:
                break
    return list
