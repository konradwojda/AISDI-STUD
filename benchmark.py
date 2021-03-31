import timeit
from matplotlib import pyplot as plt


ins_lst = []
qck_lst = []
shell_lst = []
words_numbers = [10, 100, 1000, 2000, 3000, 4000, 5000, 6000]
n_lst = []
for i in range(len(words_numbers)):
    x = words_numbers[i]
    n_lst.append(x)
    sorting_func = f'''
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from quicksort_recursive import quicksort
from model_i import import_words
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

plt.plot(n_lst, ins_lst, label='insertion sort', markersize=3)
plt.plot(n_lst, qck_lst, label='quick sort', markersize=3)
plt.plot(n_lst, shell_lst, label='shell sort', markersize=3)
plt.xticks(n_lst)
plt.legend()
plt.show()

# print(timeit.timeit('insertion_sort(list)', setup=sorting_func1, number=1))