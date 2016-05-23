# -*- coding: utf-8 -*-
import re
from collections import OrderedDict


def get_data(line):
    rule = None
    data = line.split('=>')
    if len(data) == 2:
        rule = {data[0].strip(): data[1].strip()}
    elif len(data) == 1:
        rule = data[0].strip()
    return rule


def get_rules():
    input_file = open('day19.txt', 'r')
    rules = []
    for line in input_file.readlines():
        data = get_data(line.strip())
        if data:
            rules.append(data)
    return rules


def update_molecules(starting, rule, molecules):
    (key, value) = rule.items()[0]
    occurences = [m.start() for m in re.finditer(key, starting)]
    for index in occurences:
        molecule = starting[:index] + value + starting[index + len(key):]
        molecules.add(molecule)
    return molecules


def count_distinct_molecules():
    rules = get_rules()
    starting_molecule = rules.pop(-1)
    molecules = set()
    for rule in rules:
        molecules = update_molecules(starting_molecule, rule, molecules)
    molecules_count = len(list(molecules))
    print 'Possible molecules to create: %s' % molecules_count



if __name__ == '__main__':
    count_distinct_molecules()

