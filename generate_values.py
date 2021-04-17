from random import randint


def generate_random_numbers(count):
    return [randint(-10000, 10000) for x in range(count)]


def generate_ascending_numbers(count):
    result = []
    for x in range(count):
        if x == 0:
            result.append(randint(-10000, 10000))
        else:
            result.append(randint(result[x-1], 10000))
    return result
