# -*- coding: utf-8 -*-


def get_questionaries():
    data_file = open('day06.txt', 'r')
    questionaries = []
    questions = []

    for line in data_file.readlines():
        if line.strip() == '':
            questionaries.append(questions)
            questions = []
        else:
            questions.append(set(line.strip()))

    data_file.close()
    return questionaries


def count_positive_questionaries():
    yes_count = 0
    common_count = 0
    questionaries = get_questionaries()
    for questions in questionaries:
        yes_set = set()
        for question in questions:
            yes_set = yes_set | question
        common_set = questions[0].intersection(*questions[1:])
        yes_count += len(yes_set)
        common_count += len(common_set)

    return (yes_count, common_count)


if __name__ == '__main__':
    yes_count, common_count = count_positive_questionaries()
    print('Questions with "yes" answer count is {}...'.format(yes_count))
    print('Questions with common "yes" answer count is {}...'.format(
        common_count))

