# -*- coding: utf-8 -*-

def count_floor_and_basement(input_data):
    counter = 0
    basement = -1
    basement_found = False
    for i, ch in enumerate(input_data):
        if ch == '(':
            counter += 1
        elif ch == ')':
            counter -= 1
        if counter == -1 and not basement_found:
            basement = i+1
            basement_found = True
    return (counter, basement)

def get_floor_and_first_basement():
    input_file = open('day01.txt', 'r')
    input_data = input_file.readline()
    floor, basement = count_floor_and_basement(input_data)
    print 'Floor: %s\nBasement: %s' % (floor, basement)


if __name__ == '__main__':
    get_floor_and_first_basement()

