# -*- coding: utf-8 -*-

class GiftDeliverySystem(object):

    def __init__(self):
        self.visited_santa_house = (0, 0)
        self.visited_robo_house = (0, 0)
        self.distinct_houses = [(0, 0)]

    def get_new_house(self, direction, visited):
        new_house = None
        if direction == '^':
            new_house = (visited[0], visited[1] + 1)
        elif direction == 'v':
            new_house = (visited[0], visited[1] - 1)
        elif direction == '>':
            new_house = (visited[0] + 1, visited[1])
        elif direction == '<':
            new_house = (visited[0] - 1, visited[1])
        return new_house

    def set_visited(self, next_house, santa):
        if next_house not in self.distinct_houses:
            self.distinct_houses.append(next_house)
        if santa == 'santa':
            self.visited_santa_house = next_house
        elif santa == 'robo':
            self.visited_robo_house = next_house

    def visit_new_house(self, direction, santa):
        visited = self.visited_santa_house
        if santa == 'robo':
            visited = self.visited_robo_house
        next_house = self.get_new_house(direction, visited)
        if next_house:
            self.set_visited(next_house, santa)

    def pairwise(self, santas_path):
        path = iter(santas_path)
        while True:
            yield next(path), next(path)

    def follow_one_path(self, santas_path):
        for direction in santas_path:
            self.visit_new_house(direction, 'santa')
        return len(self.distinct_houses)

    def follow_two_paths(self, santas_path):
        path = self.pairwise(santas_path)
        for santa, santa2 in path:
            self.visit_new_house(santa, 'santa')
            self.visit_new_house(santa2, 'robo')
        return len(self.distinct_houses)

    def count_santa_houses_alone(self):
        input_file = open('day03.txt', 'r')
        visited_houses_count = self.follow_one_path(input_file.readline())
        print 'Visited houses: %s' % visited_houses_count

    def count_santa_and_robo_houses(self):
        input_file = open('day03.txt', 'r')
        visited_houses_count = self.follow_two_paths(input_file.readline())
        print 'Visited houses: %s' % visited_houses_count

if __name__ == '__main__':
    GiftDeliverySystem().count_santa_houses_alone()
    GiftDeliverySystem().count_santa_and_robo_houses()

