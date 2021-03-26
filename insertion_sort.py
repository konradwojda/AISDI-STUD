"""
Algorytm sortowania przez wstawianie
Bierzemy każdy element po kolei począwszy od drugiego,
następnie "przesuwamy" w prawo elementy o indeksach mniejszych
od danego, dopóki są one od niego większe. Gdy pojawi się element mniejszy,
wstawiamy w to miejsce nasz aktualnie porównywany.
"""


def insertion_sort(list):
    for i in range(1, len(list)):
        actual_elem = list[i]
        j = i-1
        while j >= 0 and actual_elem < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = actual_elem
    return list
