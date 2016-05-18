# -*- coding: utf-8 -*-
from copy import deepcopy


MFSCAM_OUTPUT = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def get_aunts(input_file):
    aunts = []
    for line in input_file.readlines():
        data = line.strip('\n').split()
        aunt = {}
        aunt[data[1]] = {
            data[2][:-1]: int(data[3][:-1]),
            data[4][:-1]: int(data[5][:-1]),
            data[6][:-1]: int(data[7])
        }
        aunts.append(aunt)
    return aunts


def eliminate_wrong_aunts(aunt, missing_aunt):
    global MFSCAM_OUTPUT
    for key, value in MFSCAM_OUTPUT.iteritems():
        compound = aunt.values()[0].get(key)
        if compound is not None and compound != value and aunt in missing_aunt:
            missing_aunt.remove(aunt)
    return missing_aunt


def get_aunt_data(aunts):
    missing_aunt = aunts
    while len(missing_aunt) != 1:
        for aunt in aunts:
            eliminate_wrong_aunts(aunt, missing_aunt)
    return missing_aunt


def eliminate_new_wrong_aunts(aunt, missing_aunt):
    global MFSCAM_OUTPUT
    for key, value in MFSCAM_OUTPUT.iteritems():
        compound = aunt.values()[0].get(key)
        if (
            (compound is not None) and (aunt in missing_aunt) and
            (key in ['cats', 'trees']) and (compound <= value)
        ):
            missing_aunt.remove(aunt)
        elif (
            (compound is not None) and (aunt in missing_aunt) and
            (key in ['pomeranians', 'goldfish']) and (compound >= value)
        ):
            missing_aunt.remove(aunt)
        elif (
            compound is not None and aunt in missing_aunt and
            key not in ['pomeranians', 'goldfish', 'cats', 'trees'] and
            compound != value
        ):
            missing_aunt.remove(aunt)
    return missing_aunt


def get_new_aunt_data(aunts):
    missing_aunt = aunts
    while len(missing_aunt) != 1:
        for aunt in aunts:
            eliminate_new_wrong_aunts(aunt, missing_aunt)
    return missing_aunt


def find_my_aunt():
    input_file = open('day16.txt', 'r')
    aunts = get_aunts(input_file)
    missing_aunt = get_aunt_data(deepcopy(aunts))
    new_missing_aunt = get_new_aunt_data(deepcopy(aunts))

    print 'My dear missing aunt is: %s' % missing_aunt
    print 'My new dear missing aunt is: %s' % new_missing_aunt


if __name__ == '__main__':
    find_my_aunt()

