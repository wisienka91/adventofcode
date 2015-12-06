# -*- coding: utf-8 -*-

class Illumination(object):

    COLUMNS = 1000
    ROWS = 1000
    INSTRUCTIONS = ['turn on ', 'turn off ', 'toggle ']

    def __init__(self):
        self.light_grid = [
            [[0, 0] for x in range(self.ROWS)] for x in range(self.COLUMNS)
        ]

    def sanitize_line(self, line):
        trash = ['\n', ' through']
        line = line.rstrip('\n')
        line = line.replace(' through ', ',')
        return line


    def get_instructions(self, line):
        instruction = ''
        positions = []
        sanitized_line = self.sanitize_line(line)

        for i in self.INSTRUCTIONS:
            if sanitized_line.startswith(i):
                instruction = i
                sanitized_line = sanitized_line.strip(i)
        startx, starty, endx, endy = sanitized_line.split(',')
        return [
            instruction, (int(startx), int(starty)), (int(endx), int(endy))
        ]

    def change_state(self, coordinates, state):
        startx = coordinates[0][0]
        starty = coordinates[0][1]
        endx = coordinates[1][0] + 1
        endy = coordinates[1][1] + 1

        if state == 'on':
            for x in range(startx, endx):
                for y in range(starty, endy):
                    self.light_grid[x][y][0] = 1
                    self.light_grid[x][y][1] += 1
        elif state == 'off':
            for x in range(startx, endx):
                for y in range(starty, endy):
                    self.light_grid[x][y][0] = 0
                    if self.light_grid[x][y][1] > 0:
                        self.light_grid[x][y][1] -= 1
        elif state == 'toggle':
            for x in range(startx, endx):
                for y in range(starty, endy):
                    self.light_grid[x][y][0] = 1 - self.light_grid[x][y][0]
                    self.light_grid[x][y][1] += 2

    def apply_instructions(self, instructions):
        coordinates = (instructions[1], instructions[2])
        if instructions[0] == 'turn on ':
            self.change_state(coordinates, 'on')
        elif instructions[0] == 'turn off ':
            self.change_state(coordinates, 'off')
        elif instructions[0] == 'toggle ':
            self.change_state(coordinates, 'toggle')

    def apply_santa_directives(self, input_file):
        for line in input_file.readlines():
            instructions = self.get_instructions(line)
            self.apply_instructions(instructions)

    def count_lights_and_brightness(self):
        lights_on = 0
        brightness_sum = 0
        for x in range(self.COLUMNS):
            for y in range(self.COLUMNS):
                brightness_sum += self.light_grid[x][y][1]
                if self.light_grid[x][y][0] == 1:
                    lights_on += 1
        return (lights_on, brightness_sum)

    def get_lights_on_count(self):
        input_file = open('day06.txt', 'r')
        self.apply_santa_directives(input_file)
        print 'There is %s lights on' % self.count_lights_and_brightness()[0]
        print 'Brightnesses sum: %s' % self.count_lights_and_brightness()[1]

if __name__ == '__main__':
    Illumination().get_lights_on_count()

