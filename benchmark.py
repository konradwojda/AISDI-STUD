import timeit
from matplotlib import pyplot as plt

numbers_counts = [10, 100, 1000, 2000, 3000, 4000, 5000, 6000]

bst_add_lst = []
avl_add_lst = []
bst_find_lst = []
avl_find_lst = []

finding_list = [6230, -6524, -2880, 5641, 5882, 4267, 6700, 9347, -9323,
                7487, 1121, -9604, 8320, -5756, -8151, -3103, -8112, 4897,
                6633, -8790, -9727, -1172, -4859, -8234, -5418, 3697, 9985,
                -550, 702, -8290, -472, -3533, 3589, -8714, 7903, 5898, 9558,
                1113, 261, 710, -339, -2233, 9076, 3274, 1480, 9651, 5211, 2474,
                2361, -9498]

elements_to_find = [-2880, 9076, 3274, 1480, 3697]

functions_adding = {
    'BST(values=list)': bst_add_lst,
    'AVL(values=list)': avl_add_lst
}

functions_finding = {
    'bst.find(x)': bst_find_lst,
    'avl.find(x)': avl_find_lst
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

for i in range(len(elements_to_find)):
    x = elements_to_find[i]
    setup = f'''
from bst import BST
from avl import AVL
finding_list = [6230, -6524, -2880, 5641, 5882, 4267, 6700, 9347, -9323,
                7487, 1121, -9604, 8320, -5756, -8151, -3103, -8112, 4897,
                6633, -8790, -9727, -1172, -4859, -8234, -5418, 3697, 9985,
                -550, 702, -8290, -472, -3533, 3589, -8714, 7903, 5898, 9558,
                1113, 261, 710, -339, -2233, 9076, 3274, 1480, 9651, 5211, 2474,
                2361, -9498]
x = {x}
bst = BST(values=finding_list)
avl = AVL(values=finding_list)
'''
    for key, value in functions_finding.items():
        time = timeit.timeit(key, setup=setup, number=1)
        value.append(time)


# plt.plot(n_lst, bst_add_lst, 'o', linestyle='None', label='bst adding')
# plt.plot(n_lst, avl_add_lst, 'o', linestyle='None', label='avl adding')

plt.plot(elements_to_find, bst_find_lst, 'o', linestyle='None', label='bst finding')
plt.plot(elements_to_find, avl_find_lst, 'o', linestyle='None', label='avl finding')

plt.xticks(n_lst)
plt.legend()
plt.show()