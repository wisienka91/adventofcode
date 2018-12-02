# -*- coding: utf-8 -*-


def parse_input(line):
    return (line[0], int(line[1:]))


def is_duplicate(frequency, frequency_set):
    is_duplicate = False

    if frequency in frequency_set:
        is_duplicate = True
    else:
        frequency_set.add(frequency)

    return is_duplicate


def apply_frequency_changes(start_frequency, frequency_set):
    frequency = start_frequency
    frequency_repeated = None
    duplicate_found = False

    input_file = open('day01.txt', 'r')
    for line in input_file.readlines():
        sign, value = parse_input(line)
        if sign == '-':
            frequency -= value
        elif sign == '+':
            frequency += value
        else:
            pass

        if not duplicate_found:
            duplicate = is_duplicate(frequency, frequency_set)
            if duplicate:
                duplicate_found = True
                frequency_repeated = frequency

    return frequency, frequency_repeated


def perform_frequency_changes():
    start_frequency = 0
    frequency_set = set({start_frequency})
    start_frequencies = []
    first_duplicate = None

    while first_duplicate is None:
        frequency, first_duplicate = apply_frequency_changes(
            start_frequency, frequency_set)
        start_frequencies.append(frequency)
        start_frequency = frequency

    return start_frequencies[0], first_duplicate


if __name__ == '__main__':
    first_frequency, first_duplicate = perform_frequency_changes()
    print('First full frequency is {}'.format(first_frequency))
    print('First duplicated frequency is {}'.format(first_duplicate))

