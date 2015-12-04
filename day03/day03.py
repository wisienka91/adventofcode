# -*- coding: utf-8 -*-

class GiftDeliverySystem(object):
    visited_santa_house = (0, 0)
    visited_robo_house = (0, 0)
    distinct_santa_houses = [(0, 0)]

    def get_new_house(self, direction):
        new_houses = [None, None]
        if direction == '^':
            new_houses[0] = (
                self.visited_santa_house[0], self.visited_santa_house[1] + 1)
        elif direction == 'v':
            new_houses[0] = (
                self.visited_santa_house[0], self.visited_santa_house[1] - 1)
        elif direction == '>':
            new_houses[0] = (
                self.visited_santa_house[0] + 1, self.visited_santa_house[1])
        elif direction == '<':
            new_houses[0] = (
                self.visited_santa_house[0] - 1, self.visited_santa_house[1])
        return new_houses

    def check_new_santa_house(self, direction):
        next_santa_house = self.get_new_house(direction)[0]
        if (next_santa_house and 
            (next_santa_house not in self.distinct_santa_houses)
        ):
            self.distinct_santa_houses.append(next_santa_house)

        self.visited_santa_house = next_santa_house


    def get_distinct_houses(self, santas_path):
        for direction in santas_path:
            self.check_new_santa_house(direction)
        return len(self.distinct_santa_houses)

    def count_santa_houses_alone(self):
        input_file = open('day03.txt', 'r')
        visited_houses_count = self.get_distinct_houses(input_file.readline())
        print 'Visited houses: %s' % visited_houses_count

    def count_santa_and_robo_houses(self):
        return None

if __name__ == "__main__":
    GiftDeliverySystem().count_santa_houses_alone()
    GiftDeliverySystem().count_santa_and_robo_houses()

