# -*- coding: utf-8 -*-
from itertools import combinations


def _get_the_numbers():
    numbers = []
    data_file = open('day01.txt', 'r')

    for line in data_file.readlines():
        numbers.append(int(line))
    data_file.close()

    return numbers


def find_the_sum_product(sum_for_product, amount):
    numbers = _get_the_numbers()
    answer = None
    product = 1
    addends = combinations(numbers, amount)

    for i in addends:
        if sum(i) == sum_for_product:
            answer = i
    for j in answer:
        product *= j

    return product


if __name__ == '__main__':
    sum_for_product = 2020
    sum_2_product = find_the_sum_product(sum_for_product, 2)
    sum_3_product = find_the_sum_product(sum_for_product, 3)
    print('Product of 2020 two numbers sum is: {}'.format(sum_2_product))
    print('Product of 2020 three numbers sum is: {}'.format(sum_3_product))

