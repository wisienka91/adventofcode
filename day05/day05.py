# -*- coding: utf-8 -*-


def has_3_vowels(string):
    vowels = 'aeiou'
    count = 0
    for ch in string:
        if ch in vowels:
            count += 1
    if count > 2:
        return True
    return False


def has_doubled_char(string):
    previous_ch = '*'
    for ch in string:
        if ch == previous_ch:
            return True
        previous_ch = ch
    return False


def has_not_forbidden_substrings(string):
    forbidden_substrings = ['ab', 'cd', 'pq', 'xy']
    for forbidden_substring in forbidden_substrings:
        if forbidden_substring in string:
            return False
    return True


def is_string_nice(string):
    return (
        has_3_vowels(string) and has_doubled_char(string) and
        has_not_forbidden_substrings(string)
    )


def get_without_checked(index, string):
    output = bytearray(string)
    output[index] = '*'
    output[index + 1] = '*'
    return output


def has_two_same_pairs(string):
    for ch_index, ch in enumerate(string[:-2]):
        adjusted_string = get_without_checked(ch_index, string)
        chch = '%s%s' % (ch, string[ch_index+1])
        if chch in adjusted_string:
            return True
    return False


def has_repetition_after_one(string):
    for ch_index, ch in enumerate(string[:-3]):
        if ch == string[ch_index + 2]:
            return True
    return False


def is_string_new_nice(string):
    return has_two_same_pairs(string) and has_repetition_after_one(string)


def get_nice_count(input_file):
    nice_strings = 0
    new_nice_strings = 0
    for line in input_file.readlines():
        if is_string_nice(line):
            nice_strings += 1
        if is_string_new_nice(line):
            new_nice_strings += 1
    return (nice_strings, new_nice_strings)


def count_nice_strings():
    input_file = open('day05.txt', 'r')
    nice_strings = get_nice_count(input_file)
    print '%s nice strings' % nice_strings[0]
    print '%s new nice strings' % nice_strings[1]


if __name__ == '__main__':
    count_nice_strings()

