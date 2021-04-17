import timeit
from matplotlib import pyplot as plt

numbers_counts = [10, 100, 1000, 2000, 3000, 4000, 5000, 6000]

bst_add_lst = []
avl_add_lst = []
bst_find_lst = []
avl_find_lst = []

functions_adding = {
    'BST(values=list)': bst_add_lst,
    #'AVL(values=list)': avl_add_lst
}

functions_finding = {
    'bst.find(sth)': bst_find_lst,
    'avl.find(sth)': avl_find_lst
}

n_lst = []

for i in range(len(numbers_counts)):
    x = numbers_counts[i]
    n_lst.append(x)
    setup = f'''
from bst import BST
from avl import AVL
from generate_values import generate_random_numbers, generate_ascending_numbers
n = {x}
list = generate_random_numbers(n)
'''
    for key, value in functions_adding.items():
        time = timeit.timeit(key, setup=setup, number=1)
        value.append(time)


plt.plot(n_lst, bst_add_lst, 'o', linestyle='None', label='bst adding')
#plt.plot(n_lst, avl_add_lst, label='avl adding', markersize=3)
plt.xticks(n_lst)
plt.legend()
plt.show()