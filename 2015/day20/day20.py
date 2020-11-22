# -*- coding: utf-8 -*-
from math import floor, sqrt


def get_number_of_presents():
    filename = open('day20.txt', 'r')
    return int(filename.readline().strip())


def get_divisors_sum(lowest):
    dsum = 0
    bound = int(sqrt(lowest) + 1)
    for i in range(1, bound + 1, 1):
        if (lowest % i == 0):
            dsum += i
            dsum += lowest // i
    return dsum * 10


def get_divisors_sum_tweaked(lowest):
    dsum = 0
    bound = int(sqrt(lowest) + 1)
    for i in range(1, bound + 1, 1):
        if (lowest % i == 0):
            if (i <= 50):
                dsum += lowest // i
            if (lowest // i <= 50):
                dsum += i
    return dsum * 11


def has_enough_presents(lowest, n, mode):
    dsum = 0
    if mode == 'normal':
        dsum = get_divisors_sum(lowest)
    else:
        dsum = get_divisors_sum_tweaked(lowest)
    if dsum >= n:
        return True
    return False


def get_lowest_house_number(n):
    lowest = n // 50
    lowest_tweaked = n // 50
    while not has_enough_presents(lowest, n, 'normal'):
        lowest += 1
    while not has_enough_presents(lowest_tweaked, n, 'tweaked'):
        lowest_tweaked += 1
    return (lowest, lowest_tweaked)


def get_lowest_house_number_with_n_presents(n):
    lowest_house_number, lowest_house_number_tweaked = get_lowest_house_number(n)
    print('Lowest house number with {} presents: {}'.format(
        n, lowest_house_number))
    print('Lowest house number tweaked with {} presents: {}'.format(
        n, lowest_house_number_tweaked))


if __name__ == '__main__':
    n = get_number_of_presents()
    get_lowest_house_number_with_n_presents(n)

