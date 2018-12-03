# -*- coding: utf-8 -*-
import itertools


def get_line_letter_map(line):
    line_letter_map = {}
    for ch in line.rstrip():
        if ch in list(line_letter_map.keys()):
            line_letter_map[ch] += 1
        else:
            line_letter_map[ch] = 1
    return line_letter_map


def count_two_and_three(line_letter_map):
    line_occurrences = list(line_letter_map.values())
    l2 = line_occurrences.count(2)
    l3 = line_occurrences.count(3)
    return l2, l3


def get_checksum(data):
    two = 0
    three = 0
    for line in data:
        line_letter_map = get_line_letter_map(line)
        l2, l3 = count_two_and_three(line_letter_map)
        if l2 > 0:
            two += 1
        if l3 > 0:
            three += 1

    return two * three


def match_enough(string1, string2):
    is_match_enough = False
    diff_index = None
    comparison = [string1[i] != string2[i] for i in range(len(string1))]
    s = sum(comparison)
    if s == 1:
        is_match_enough = True
        diff_index = comparison.index(True)
    return (is_match_enough, diff_index)


def get_similars_and_index(data):
    similars = None
    match_found = False
    diff_index = None
    combinations = itertools.product(data, data)

    for com in combinations:
        match_found, diff_index = match_enough(com[0], com[1])
        if match_found:
            similars = (com[0].rstrip(), com[1].rstrip())
            break

    return (similars, diff_index)


def get_box_id(data):
    similars, diff_index = get_similars_and_index(data)
    box_id = similars[0][:diff_index] + similars[0][diff_index + 1:]
    return box_id


if __name__ == '__main__':
    input_file = open('day02.txt', 'r')
    data = input_file.readlines()
    checksum = get_checksum(data)
    box_id = get_box_id(data)
    print("Checksum is: {}".format(checksum))
    print("Box id is: {}".format(box_id))

