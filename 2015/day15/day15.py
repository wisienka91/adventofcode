# -*- coding: utf-8 -*-
import itertools


def build_ingredient(data):
    return {
            data[1]: int(data[2]),
            data[3]: int(data[4]),
            data[5]: int(data[6]),
            data[7]: int(data[8]),
            data[9]: int(data[10])
        }


def get_ingredients(input_file):
    ingredients = []
    for line in input_file.readlines():
        data = line.strip('\n').replace(',', '').split()
        ingredient = build_ingredient(data)
        ingredients.append(ingredient)
    return ingredients


def count_ingredients_without_calories(i, ingredients, option, svalues, svalue):
    ssum = 1
    skeys = [key for key in ingredients[i].keys() if key != 'calories']
    for key in skeys:
        if key != 'calories':
            ing = [ingredients[j][key] for j in range(i+2)]
            psum = sum([a * b for a, b in zip(option, ing)])
            ssum = ssum * psum if psum > 0 else ssum
    if ssum > svalue:
        svalues.append((option, ssum))
        svalue = max(item[1] for item in svalues)
    return ssum


def count_ingredients_with_calories(
    i, ingredients, option, cvalues, cvalue, ssum):
    csum = 0
    ckeys = [key for key in ingredients[i].keys() if key == 'calories']
    for key in ckeys:
        if key == 'calories':
            ing = [ingredients[j]['calories'] for j in range(i+2)]
            csum = sum([a * b for a, b in zip(option, ing)])
    if ssum > cvalue and csum == 500:
        cvalues.append((option, ssum))
        cvalue = max(item[1] for item in cvalues)
    return csum


def count_option_values(ingredients, option, svalues, cvalues, svalue, cvalue):
    for i in range(len(ingredients) - 1):
        ssum = count_ingredients_without_calories(
            i, ingredients, option, svalues, svalue)
        csum = count_ingredients_with_calories(
            i, ingredients, option, cvalues, cvalue, ssum)
    return (svalues, cvalues)


def count_proportions(ingredients, options):
    svalues = [(0, 0)]
    cvalues = [(0, 0)]
    for option in options:
        svalue = max(item[1] for item in svalues)
        cvalue = max(item[1] for item in cvalues)
        svalues, cvalues = count_option_values(
            ingredients, option, svalues, cvalues, svalue, cvalue)
    return (svalues, cvalues)


def get_proportions(ingredients):
    sample = [i for i in range(101)]
    options = (j for j in itertools.product(
        sample, repeat=len(ingredients)) if sum(j) == 100
    )
    return count_proportions(ingredients, options)


def get_perfect_cookie_ingredients_proportions():
    input_file = open('day15.txt', 'r')
    ingredients = get_ingredients(input_file)
    sresult, cresult = get_proportions(ingredients)
    sbest = max(item[1] for item in sresult)
    cbest = max(item[1] for item in cresult)
    print 'The perfect cookie result is: %s.' % sbest
    print 'The perfect cookie with calories result is: %s.' % cbest


if __name__ == '__main__':
    get_perfect_cookie_ingredients_proportions()

