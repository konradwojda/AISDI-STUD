import timeit
from matplotlib import pyplot as plt
from generate_values import generate_random_numbers, generate_ascending_numbers

numbers_counts = [10000, 50000, 100000, 250000, 500000]

bst_add_lst = []
avl_add_lst = []
bst_add_lst_final = []
avl_add_lst_final = []
bst_find_lst = []
avl_find_lst = []

elements_to_find = [100, 500, 1000, 5000, 10000, 25000, 40000, 60000, 80000, 90000, 99999]

values_to_add = [-10, 10.5, 50.5, 500.5, 200000.5]

functions_adding = {
    'bst.add(y)': bst_add_lst,
    'avl.add(y)': avl_add_lst
}

functions_finding = {
    'bst.find(list[x])': bst_find_lst,
    'avl.find(list[x])': avl_find_lst
}

n_lst = []

def benchmark_adding(data_type: str):
    for i in range(len(numbers_counts)):
        x = numbers_counts[i]
        n_lst.append(x)
        lst = generate_ascending_numbers(x)
        lst_str = str(lst)
        for element in values_to_add:
            setup = f'''
from bst import BST
from avl import AVL
y = {element}
bst = BST(values={lst_str})
avl = AVL(values={lst_str})
'''
            for key, value in functions_adding.items():
                    time = timeit.timeit(key, setup=setup, number=1)
                    value.append(time)
        avl_time = sum(avl_add_lst) / len(avl_add_lst)
        bst_time = sum(bst_add_lst) / len(bst_add_lst)
        avl_add_lst.clear()
        bst_add_lst.clear()
        avl_add_lst_final.append(avl_time)
        bst_add_lst_final.append(bst_time)
    plt.plot(n_lst, bst_add_lst_final, 'o', linestyle='None', label='bst adding')
    plt.plot(n_lst, avl_add_lst_final, 'o', linestyle='None', label='avl adding')
    plt.xticks(n_lst)
    print('Suma czasów:\n')
    print('Drzewo AVL:')
    print(str(sum(avl_add_lst_final)) + '\n')
    print('Drzewo BST:')
    print(str(sum(bst_add_lst_final)) + '\n')

def benchmark_finding(data_type: str):
    for element in elements_to_find:
        x = element
        setup = f'''
from bst import BST
from avl import AVL
from generate_values import generate_random_numbers, generate_ascending_numbers
list = generate_{data_type}_numbers(10000)
x = {x}
bst = BST(values=list)
avl = AVL(values=list)
'''
        for key, value in functions_finding.items():
            time = timeit.timeit(key, setup=setup, number=1)
            value.append(time)
    plt.plot(elements_to_find, bst_find_lst, 'o', linestyle='None', label='bst finding')
    plt.plot(elements_to_find, avl_find_lst, 'o', linestyle='None', label='avl finding')
    print('Suma czasów:\n')
    print('Drzewo AVL:')
    print(str(sum(avl_find_lst)) + '\n')
    print('Drzewo BST:')
    print(str(sum(bst_find_lst)) + '\n')


if __name__ == '__main__':
    benchmark_finding('random')
    plt.legend()
    plt.show()