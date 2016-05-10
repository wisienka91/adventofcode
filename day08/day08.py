# -*- coding: utf-8 -*-

def get_characters_count(line):
    return len(line[:-1])

def get_decoded_count(line):
    return len(line.decode('string-escape')[1:-2])

def get_encoded_count(line):
    count = len(line[:-1]) + 2
    for i, c in enumerate(line[:-1]):
        if c == '\\' and line[i] == 'x':
            count += 1
        elif c == '\\':
            count += 1
        elif c == '"':
            count += 1
    return count

def get_count(input_file):
    characters_count = 0
    decoded_count = 0
    encoded_count = 0
    for line in input_file:
        characters_count += get_characters_count(line)
        decoded_count += get_decoded_count(line)
        encoded_count += get_encoded_count(line)
    return (characters_count - decoded_count, encoded_count - characters_count)

def count_characters_without_decoded():
    input_file = open('day08.txt', 'r')
    escaped, nonescaped = get_count(input_file)
    print 'Characters without escaped literals: %s' % escaped
    print 'Characters encoded without characters: %s' % nonescaped

if __name__ == '__main__':
    count_characters_without_decoded()

