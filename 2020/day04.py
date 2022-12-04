# -*- coding: utf-8 -*-
import utils
import re

input = utils.get_input(4)


# input = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
#
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
#
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
#
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in'''


def first():
    passports = input.split('\n\n')
    valid_passports = 0
    for passport in passports:
        num_of_fields = 0
        has_cid = False
        lines = passport.split('\n')
        for line in lines:
            fields = line.split(' ')
            for field in fields:
                parts = field.split(':')
                field_name = parts[0]
                num_of_fields += 1
                if field_name == 'cid':
                    has_cid = True
        if num_of_fields == 8 or (num_of_fields == 7 and not has_cid):
            valid_passports += 1
    return valid_passports


def second():
    passports = input.split('\n\n')
    valid_passports = 0
    for passport in passports:
        num_of_fields = 0
        has_cid = False
        lines = passport.split('\n')
        is_valid = True
        for line in lines:
            fields = line.split(' ')
            for field in fields:
                parts = field.split(':')
                field_name = parts[0]
                value = parts[1]
                if field_name in 'cid byr iyr eyr hgt hcl ecl pid'.split(' '):
                    num_of_fields += 1
                if field_name == 'cid':
                    has_cid = True
                elif field_name == 'byr':
                    value = int(value)
                    if value < 1920 or value > 2002:
                        is_valid = False
                elif field_name == 'iyr':
                    value = int(value)
                    if value < 2010 or value > 2020:
                        is_valid = False
                elif field_name == 'eyr':
                    value = int(value)
                    if value < 2020 or value > 2030:
                        is_valid = False
                elif field_name == 'hgt':
                    matches = re.match('(\d+)(cm|in)', value)
                    if not matches:
                        is_valid = False
                        continue
                    matches = matches.groups()
                    height = int(matches[0])
                    if matches[1] == 'cm':
                        if height < 150 or height > 193:
                            is_valid = False
                    elif matches[1] == 'in':
                        if height < 59 or height > 76:
                            is_valid = False
                    else:
                        is_valid = False
                elif field_name == 'hcl':
                    matches = re.match('^\#[0-9a-f]{6,6}$', value)
                    if not matches:
                        is_valid = False
                elif field_name == 'ecl':
                    if value not in 'amb blu brn gry grn hzl oth'.split(' '):
                        is_valid = False
                elif field_name == 'pid':
                    matches = re.match('^[0-9]{9,9}$', value)
                    if not matches:
                        is_valid = False

        if is_valid and (num_of_fields == 8 or (num_of_fields == 7 and not has_cid)):
            valid_passports += 1
    return valid_passports


if __name__ == '__main__':
    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
