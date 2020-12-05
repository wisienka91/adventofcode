# -*- coding: utf-8 -*-
import re


def get_passports_data():
    passports = []
    passport = {}
    data_file = open('day04.txt', 'r')

    for line in data_file.readlines():
        if line.strip():
            for raw_data in line.strip().split(" "):
                data = raw_data.split(":")
                passport[data[0]] = data[1]
        else:
            passports.append(passport)
            passport = {}

    data_file.close()
    return passports


def _check_elements(passport):
    elements = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    checked = elements.issubset(set(passport.keys())) 
    return checked


def _hgt_validate(hgt):
    validated = False
    if hgt.endswith('cm') and (150 <= int(hgt[:-2]) <= 193):
        validated = True
    elif hgt.endswith('in') and (59 <= int(hgt[:-2]) <= 76):
        validated = True
    else:
        pass
    return validated


def _validate_values(passport):
    validated = True

    byr = passport.get('byr')
    iyr = passport.get('iyr')
    eyr = passport.get('eyr')
    hgt = passport.get('hgt')
    hcl = passport.get('hcl')
    ecl = passport.get('ecl')
    pid = passport.get('pid')

    if not (byr and (1920 <= int(byr) <= 2002)):
        validated = False

    if not (iyr and (2010 <= int(iyr) <= 2020)):
        validated = False

    if not (eyr and (2020 <= int(eyr) <= 2030)):
        validated = False

    if not (hgt and _hgt_validate(hgt)):
        validated = False

    if not(hcl and re.match('#[a-f0-9]{6}', hcl)):
        validated = False

    if not(ecl and (ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])):
        validated = False

    if not(pid and (len(pid) == 9)):
        validated = False

    return validated


def count_valid_passports():
    count_correct_fields = 0
    count_valid_values = 0

    passports = get_passports_data()

    for passport in passports:
        if _check_elements(passport):
            count_correct_fields += 1
        if _validate_values(passport):
            count_valid_values += 1

    return (count_correct_fields, count_valid_values)


if __name__ == '__main__':
    valid_fields_passports, valid_values_passports = count_valid_passports()
    print('There is {} valid fields passwords...'.format(valid_fields_passports))
    print('There is {} valid values passwords...'.format(valid_values_passports))

