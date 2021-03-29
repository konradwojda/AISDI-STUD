import timeit
from matplotlib import pyplot as plt


ins_lst = []
qck_lst = []
shell_lst = []
x = 1000
n_lst = []
for i in range(5):
    n_lst.append(x)
    sorting_func = f'''
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from quicksort_recursive import quicksort
from import_words import import_words
n = {x}
list = import_words('pan-tadeusz.txt', n)
'''
    temp_times = []
    # ins sort
    for _ in range(4):
        time = timeit.timeit('insertion_sort(list)', setup=sorting_func, number=1)
        temp_times.append(time)
    temp_times.remove(max(temp_times))
    temp_times.remove(min(temp_times))
    time = (temp_times[0] + temp_times[1])/2
    ins_lst.append(time)
    temp_times = []
    # qck sort
    for _ in range(4):
        time = timeit.timeit('quicksort(list)', setup=sorting_func, number=1)
        temp_times.append(time)
    temp_times.remove(max(temp_times))
    temp_times.remove(min(temp_times))
    time = (temp_times[0] + temp_times[1])/2
    qck_lst.append(time)
    temp_times = []
    # shell sort
    for _ in range(4):
        time = timeit.timeit('shell_sort(list)', setup=sorting_func, number=1)
        temp_times.append(time)
    temp_times.remove(max(temp_times))
    temp_times.remove(min(temp_times))
    time = (temp_times[0] + temp_times[1])/2
    shell_lst.append(time)
    # if i == 0:
    #     x = x * 10
    # if i > 0 and i < 10:
    #     x = x + 100
    # if i > 10:
    x = x + 1000

plt.plot(n_lst, ins_lst, label='insertion sort', markersize=3)
plt.plot(n_lst, qck_lst, label='quick sort', markersize=3)
plt.plot(n_lst, shell_lst, label='shell sort', markersize=3)
plt.xticks(n_lst)
plt.legend()
plt.show()

# print(timeit.timeit('insertion_sort(list)', setup=sorting_func1, number=1))
