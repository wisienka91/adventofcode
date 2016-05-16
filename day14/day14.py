# -*- coding: utf-8 -*-


def get_reindeers(input_file):
    reindeers = {}
    for line in input_file.readlines():
        data = line.split()
        reindeers[data[0]] = {
            'speed': int(data[3]),
            'runtime': int(data[6]),
            'resttime': int(data[-2])
        }
    return reindeers


def reindeer_run_in_time(reindeer, seconds):
    run_time = 0
    distance = 0
    while run_time < seconds:
        if seconds - run_time < reindeer['runtime']:
            distance += reindeer['speed'] * (seconds - run_time)
            run_time += (seconds - run_time)
        else:
            distance += reindeer['speed'] * reindeer['runtime']
            run_time += reindeer['runtime']
        if run_time < seconds:
            run_time += reindeer['resttime']
    return distance


def run_for_distance(reindeers, seconds):
    results = {}
    for reindeer_name in reindeers:
        reindeer = reindeers.get(reindeer_name)
        results[reindeer_name] = reindeer_run_in_time(reindeer, seconds)
    return results


def get_distances_after_time(reindeers, second):
    distances = {}
    for reindeer_name in reindeers:
        reindeer = reindeers.get(reindeer_name)
        distances[reindeer_name] = reindeer_run_in_time(reindeer, second)
    return distances


def get_current_max_distance(distances, max_distance):
    for distance in distances.values():
        max_distance = distance if distance >= max_distance else max_distance
    return max_distance


def update_scoreboard(scoreboard, reindeers, distances, max_distance):
    for name in reindeers:
        scoreboard[name] = scoreboard[name] + 1 if distances[
            name] == max_distance else scoreboard[name]
    return scoreboard


def run_for_points(reindeers, seconds):
    scoreboard = {k: 0 for k in reindeers.keys()}
    max_distance = 0
    for second in range(1, seconds, 1):
        distances = get_distances_after_time(reindeers, second)
        max_distance = get_current_max_distance(distances, max_distance)
        scoreboard = update_scoreboard(
            scoreboard, reindeers, distances, max_distance)
    return scoreboard


def print_winner(data, units):
    winner_result = max(data.values())
    winner_name = data.keys()[data.values().index(winner_result)]
    print '\nWinner was %s with: %s%s.\nFull results are: %s.' % (
        winner_name, winner_result, units, data)


def start_a_race(seconds):
    input_file = open('day14.txt', 'r')
    reindeers = get_reindeers(input_file)

    results = run_for_distance(reindeers, seconds)
    scoreboard = run_for_points(reindeers, seconds)

    print_winner(results, 'km')
    print_winner(scoreboard, 'pts')


if __name__ == '__main__':
    start_a_race(seconds=2503)

