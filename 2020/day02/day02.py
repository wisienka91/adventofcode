# -*- coding: utf-8 -*-


def _parse_line(line):
    parsed_line = {}
    raw_line = line.strip().split(" ")

    parsed_line['min'] = int(raw_line[0].split("-")[0])
    parsed_line['max'] = int(raw_line[0].split("-")[1])
    parsed_line['letter'] = raw_line[1].strip(":")
    parsed_line['password'] = raw_line[2]

    return parsed_line


def _get_the_rules():
    rules = []
    data_file = open('day02.txt', 'r')

    for line in data_file.readlines():
        rules.append(_parse_line(line))
    data_file.close()

    return rules


def check_password_by_count(rule):
    count = rule['password'].count(rule['letter'])
    if rule['min'] <= count <= rule['max']:
        return True
    return False


def check_password_by_position(rule):
    position_a = rule['password'][rule['min'] - 1] if rule['min'] > 0 else ''
    position_b = rule['password'][rule['max'] - 1] if rule['max'] <= len(
        rule['password']) else ''

    if ((position_a == rule['letter']) ^ (position_b == rule['letter'])):
        return True
    return False


def count_correct_passwords():
    rules = _get_the_rules()
    result_count = 0
    result_position = 0

    for rule in rules:
        if check_password_by_count(rule):
            result_count += 1
        if check_password_by_position(rule):
            result_position += 1

    return (result_count, result_position)


if __name__ == '__main__':
    result_count, result_position = count_correct_passwords()
    print('There is {} correct count passwords...'.format(result_count))
    print('There is {} correct position passwords...'.format(result_position))

