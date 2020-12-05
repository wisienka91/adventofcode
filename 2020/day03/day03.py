# -*- coding: utf-8 -*-


def get_the_map():
    world_map = []
    data_file = open('day03.txt', 'r')

    for line in data_file.readlines():
        world_map.append(line.strip())
    data_file.close()

    return world_map


def count_the_trees(world_map, step_x, step_y):
    trees_count = 0

    map_length = len(world_map[0])
    map_height = len(world_map)

    t_position_x = 0
    t_position_y = 0

    while (t_position_y < map_height - step_y):
        t_position_x = t_position_x + step_x
        t_position_y = t_position_y + step_y
        if world_map[t_position_y][t_position_x % map_length] == '#':
            trees_count += 1

    return trees_count


def count_the_multislide(world_map):
    multi_slide = 1
    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for step in steps:
        multi_slide *= count_the_trees(world_map, step[0], step[1])

    return multi_slide


if __name__ == '__main__':
    world_map = get_the_map()
    trees_count = count_the_trees(world_map, step_x=3, step_y=1)
    multi_slide = count_the_multislide(world_map)
    print('There was {} trees on the snowy way down...'.format(trees_count))
    print('Multi-slide result is {}'.format(multi_slide))

