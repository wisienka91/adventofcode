# -*- coding: utf-8 -*-


def strip_newlines(line):
    for i, item in enumerate(line):
        line[i] = item.strip('\n')
    return line


def get_package_dimensions(raw_line):
    parsed_line = strip_newlines(raw_line.split('x'))
    l = int(parsed_line[0])
    w = int(parsed_line[1])
    h = int(parsed_line[2])
    return (l, w, h)


def get_smallest_side(l, w, h):
    smallest_side = l * w
    if l*h < smallest_side:
        smallest_side = l*h
    if w*h < smallest_side:
        smallest_side = w*h
    return smallest_side


def get_ribbon_wrap_amount(l, w, h):
    ribbon_wrap = 2*l + 2*w
    if (2*l + 2*h) < ribbon_wrap:
        ribbon_wrap = 2*l + 2*h
    if (2*w + 2*h) < ribbon_wrap:
        ribbon_wrap = 2*w + 2*h
    return ribbon_wrap


def count_per_package(raw_line):
    l, w, h = get_package_dimensions(raw_line)
    paper_amount = 2*l*w + 2*l*h + 2*w*h + get_smallest_side(l, w, h)
    ribbon_amount = l*w*h + get_ribbon_wrap_amount(l, w, h)
    return (paper_amount, ribbon_amount)


def sum_amounts(input_file):
    paper_amount = 0
    ribbon_amount = 0
    for line in input_file.readlines():
        amounts = count_per_package(line)
        paper_amount += amounts[0]
        ribbon_amount += amounts[1]
    return (paper_amount, ribbon_amount)


def get_paper_and_ribbon_amount():
    input_file = open('day02.txt', 'r')
    paper_amount, ribbon_amount = sum_amounts(input_file)
    print('Paper amount needed: {0}'.format(paper_amount))
    print('Ribbon amount needed: {0}'.format(ribbon_amount))


if __name__ == '__main__':
    get_paper_and_ribbon_amount()

