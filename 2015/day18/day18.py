# -*- coding: utf-8 -*-


class Ilumination2(object):

    def __init__(self, steps):
        self.rows = 100
        self.columns = 100
        self.light_grid = {}
        self.steps = steps

    def adjust_corners(self):
        self.light_grid[(0, 0)] = '#'
        self.light_grid[(0, self.rows - 1)] = '#'
        self.light_grid[(self.columns - 1, 0)] = '#'
        self.light_grid[(self.rows - 1, self.columns - 1)] = '#'

    def load_initial_state(self, corners=False):
        input_file = open('day18.txt', 'r')
        for i, line in enumerate(input_file.readlines()):
            for j, ch in enumerate(line.strip('\n')):
                self.light_grid[(i, j)] = ch
        if corners:
            self.adjust_corners()

    def count_lights_on(self):
        lights_on = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.light_grid[(i, j)] == '#':
                    lights_on += 1
        print 'Lights on: %s' % lights_on

    def get_neighbours(self, cords):
        up = [-1, 0, 1]
        down = [-1, 0, 1]
        neighbours = []
        for i in up:
            for j in down:
                if self.light_grid.get((cords[0] + i, cords[1] + j)):
                    neighbours.append((cords[0] + i, cords[1] + j))
        neighbours.remove(cords)
        return neighbours

    def count_neighbours_on(self, cords):
        neighbours = self.get_neighbours(cords)
        on = 0
        for neighbour in neighbours:
            if self.light_grid.get(neighbour) == '#':
                on += 1
        return on

    def is_corner(self, cords):
        corners = [
            (0, 0), (0, self.rows - 1),
            (self.columns - 1, 0), (self.rows - 1, self.columns - 1)
        ]
        if cords in corners:
            return True
        return False

    def get_next_state(self, cords, corners='off'):
        state = '.'
        on = [2, 3]
        neighbours_on = self.count_neighbours_on(cords)
        if corners == 'on':
            if self.is_corner(cords):
                return {cords: '#'}
        if self.light_grid.get(cords) == '#':
            if neighbours_on in on:
                state = '#'
        elif self.light_grid.get(cords) == '.':
            if neighbours_on == 3:
                state = '#'
        return {cords: state}

    def get_next_grid(self, corners='off'):
        next_grid = {}
        for cords in self.light_grid.keys():
            next_grid.update(self.get_next_state(cords, corners))
        return next_grid

    def illuminate(self):
        for step in range(self.steps):
            next_grid = self.get_next_grid()
            self.light_grid = next_grid

    def illuminate_with_corners(self):
        for step in range(self.steps):
            next_grid = self.get_next_grid(corners='on')
            self.light_grid = next_grid


if __name__ == '__main__':
    i1 = Ilumination2(100)
    i1.load_initial_state()
    i1.illuminate()
    i1.count_lights_on()
    i2 = Ilumination2(100)
    i2.load_initial_state(corners=True)
    i2.illuminate_with_corners()
    i2.count_lights_on()

