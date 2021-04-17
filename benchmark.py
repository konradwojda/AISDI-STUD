import timeit
from matplotlib import pyplot as plt

numbers_counts = [10, 100, 1000, 2000, 3000, 4000, 5000, 6000]

bst_add_lst = []
avl_add_lst = []
bst_find_lst = []
avl_find_lst = []

elements_to_find = [10, 100, 500, 1000, 2000, 5000, 6000, 10000, 15345, 19000]

functions_adding = {
    'BST(values=list)': bst_add_lst,
    'AVL(values=list)': avl_add_lst
}

functions_finding = {
    'bst.find(list[x])': bst_find_lst,
    'avl.find(list[x])': avl_find_lst
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
list = generate_ascending_numbers(n)
'''
    for key, value in functions_adding.items():
        time = timeit.timeit(key, setup=setup, number=1)
        value.append(time)

for element in elements_to_find:
    x = element
    setup = f'''
from bst import BST
from avl import AVL
from generate_values import generate_random_numbers, generate_ascending_numbers
list = generate_random_numbers(20000)
x = {x}
bst = BST(values=list)
avl = AVL(values=list)
'''
    for key, value in functions_finding.items():
        time = timeit.timeit(key, setup=setup, number=1)
        value.append(time)


# plt.plot(n_lst, bst_add_lst, 'o', linestyle='None', label='bst adding')
# plt.plot(n_lst, avl_add_lst, 'o', linestyle='None', label='avl adding')
# plt.xticks(n_lst)
plt.plot(elements_to_find, bst_find_lst, 'o', linestyle='None', label='bst finding')
plt.plot(elements_to_find, avl_find_lst, 'o', linestyle='None', label='avl finding')

print(sum(avl_find_lst))
print(sum(bst_find_lst))

plt.legend()
plt.show()