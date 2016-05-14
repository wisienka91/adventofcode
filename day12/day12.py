# -*- coding: utf-8 -*-
import json
import re


numbers_sum = 0


def handle_excluded_in_dict(obj, exclude):
    if exclude is not None:
        return {
            k: traverse(v, exclude) for k, v in obj.items()
        } if exclude not in obj.values() else None
    else:
        return {k: traverse(v) for k, v in obj.items()}


def traverse(obj, exclude=None):
    global numbers_sum
    if isinstance(obj, dict):
        handle_excluded_in_dict(obj, exclude)
    elif isinstance(obj, list):
        return [traverse(elem, exclude) for elem in obj]
    else:
        try:
            num = int(obj)
        except (TypeError, ValueError):
            pass
        else:
            numbers_sum += num
    return obj


def count(exclude=None):
    global numbers_sum
    numbers_sum = 0
    input_file = open('day12.txt', 'r')
    data = json.loads(input_file.readline())
    traverse(data, exclude)
    print 'JSON numbers count with %s excluded is %s' % (exclude, numbers_sum)


if __name__ == '__main__':
    count()
    count(exclude='red')

