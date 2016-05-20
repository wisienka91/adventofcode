# -*- coding: utf-8 -*-
import itertools


def powerset(iterable):
    return itertools.chain.from_iterable(
        itertools.combinations(iterable, r) for r in range(len(iterable) + 1)
    )


def get_containers(input_file):
    containers = []
    for line in input_file.readlines():
        containers.append(int(line.rstrip('\n')))
    return containers


def get_options_with_shortest(barrel, containers):
    options = 0
    shortest = len(containers)
    for i in powerset(containers):
        if sum(i) == barrel:
            options += 1
            shortest = len(i) if len(i) < shortest else shortest
    return (options, shortest)


def get_shortest_ways_count(barrel, containers, shortest):
    ways = 0
    for i in powerset(containers):
        ways = ways + 1 if sum(i) == barrel and len(i) == shortest else ways
    return ways 


def number_of_combinations(barrel):
    input_file = open('day17.txt', 'r')
    containers = get_containers(input_file)

    options, shortest = get_options_with_shortest(barrel, containers)
    ways = get_shortest_ways_count(barrel, containers, shortest)

    print 'Number of options: %s' % options
    print 'Number of shortest ways: %s' % ways


if __name__ == '__main__':
    number_of_combinations(150)

