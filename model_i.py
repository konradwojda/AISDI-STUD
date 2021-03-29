def import_all_words(path):
    words = []
    with open(path, 'r') as handle:
        for line in handle:
            line_lst = [word for word in line.split()]
            words += line_lst
    return words


def import_words(path, count):
    words = import_all_words(path)
    return words[:count]

def generate_sorted_numbers(count):
    numbers = []
    for i in range(1, count + 1):
        numbers.append(i)
    return numbers
