# -*- coding: utf-8 -*-
import itertools


def count_path(permutation, distances):
    general_distance = 0
    for i in range(len(permutation) - 1):
        city_distance = distances.get((permutation[i], permutation[i+1]))
        if not city_distance:
            city_distance = distances.get((permutation[i+1], permutation[i]))
        general_distance += city_distance
    return general_distance


def get_paths(cities, distances):
    shortest_path = None
    longest_path = None
    short_length = sum(distances.values())
    long_length = 0
    for permutation in itertools.permutations(cities):
        distance = count_path(permutation, distances)
        if distance < short_length:
            short_length = distance
            shortest_path = permutation
        if distance > long_length:
            long_length = distance
            longest_path = permutation
    return (shortest_path, short_length, longest_path, long_length)


def get_distance_length(line):
    raw_distance = line.split()
    return {(raw_distance[0], raw_distance[2]): int(raw_distance[4])}


def get_cities_and_distances(input_file):
    cities = []
    distances = {}
    for line in input_file.readlines():
        distance = get_distance_length(line.strip('\n'))
        if line.split()[0] not in cities:
            cities.append(line.split()[0])
        if line.split()[2] not in cities:
            cities.append(line.split()[2])
        distances.update(distance)
    return (cities, distances)


def get_shortest_path_length():
    input_file = open('day09.txt', 'r')
    cities, distances = get_cities_and_distances(input_file)
    short_path, short_len, long_path, long_len = get_paths(cities, distances)
    print 'Shortest path is: %s with length: %s.' % (short_path, short_len)
    print 'Longest path is: %s with length: %s.' % (long_path, long_len)


if __name__ == '__main__':
    get_shortest_path_length()

