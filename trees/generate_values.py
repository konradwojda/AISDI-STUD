from random import randint


def generate_random_numbers(count):
    return [randint(-10000, 10000) for x in range(count)]


def generate_ascending_numbers(count):
    return [x for x in range(count)]