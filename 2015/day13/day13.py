# -*- coding: utf-8 -*-
import itertools


def get_people_and_pairs(input_file):
    people = []
    pairs = {}
    multipliers = {'gain': 1, 'lose': -1}
    for line in input_file.readlines():
        data = line.rstrip('.\n').split()
        if data[-1] + ' ' + data[0] in pairs:
            pairs[data[-1] + ' ' + data[0]] += multipliers[
                data[2]] * int(data[3])
        else:
            pairs[data[0] + ' ' + data[-1]] = multipliers[
                data[2]] * int(data[3])
        if data[0] not in people:
            people.append(data[0])
    return (people, pairs)


def count(people, pairs, setting):
    happiness = 0
    for i in range(len(setting)):
        j = (i+1) % (len(setting))
        if setting[i] + ' ' + setting[j] in pairs:
            happiness += pairs[setting[i] + ' ' + setting[j]]
        else:
            happiness += pairs[setting[j] + ' ' + setting[i]]
    return happiness


def get_happiness(people, pairs):
    sadness = min(pairs.values())
    max_happiness =  9 * sadness if sadness < 0 else -9 * sadness
    best_setting = None
    for setting in itertools.permutations(people):
        if setting[0] == people[0]:
            best_setting = setting
            happiness = count(people, pairs, setting)
            if happiness > max_happiness:
                max_happiness = happiness
    return (max_happiness, best_setting)


def count_happiness(input_file):
    people, pairs = get_people_and_pairs(input_file)
    happiness, setting = get_happiness(people, pairs)
    print 'Optimal happiness is %s with setting: %s' % (happiness, setting)


if __name__ == '__main__':
    input_file = open('day13.txt', 'r')
    count_happiness(input_file)
    input_file2 = open('day132.txt', 'r')
    count_happiness(input_file2)

