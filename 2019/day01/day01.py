# -*- coding: utf-8 -*-


def count_fuel_for_module(module_mass):
    fuel_for_module = module_mass // 3 - 2
    return fuel_for_module


def count_fuel_for_module_and_fuel(module_fuel):
    fuel_adjusted = 0
    sub_sum = module_fuel
    while (sub_sum >= 0):
        sub_sum = sub_sum // 3 - 2
        if sub_sum >= 0:
            fuel_adjusted += sub_sum
    return fuel_adjusted


def count_all_fuel():
    fuel_sum = 0
    fuel_sum_adjusted = 0
    input_file = open('day01.txt', 'r')
    for line in input_file.readlines():
        module_mass = int(line)
        module_fuel = count_fuel_for_module(module_mass)
        fuel_sum += module_fuel
        module_fuel_adjusted = count_fuel_for_module_and_fuel(module_fuel)
        fuel_sum_adjusted += module_fuel + module_fuel_adjusted
    return (fuel_sum, fuel_sum_adjusted)

if __name__ == '__main__':
    (fuel_sum, fuel_sum_adjusted) = count_all_fuel()
    print(fuel_sum)
    print(fuel_sum_adjusted)

