# -*- coding: utf-8 -*-
import utils

input = utils.get_input_multiline_str(2)


# input = sample input

def count_char_in_str(char, string):
    count = 0
    for i in string:
        if i == char:
            count = count + 1
    return count


def first():
    valid = 0
    for line in input:
        parts = line.split(': ')
        policy = parts[0].split(' ')
        num = policy[0].split('-')
        min = int(num[0])
        max = int(num[1])
        char = policy[1]
        password = parts[1]
        num_of_char = count_char_in_str(char, password)
        if min <= num_of_char <= max:
            valid += 1
    return valid


def second():
    valid = 0
    for line in input:
        parts = line.split(': ')
        policy = parts[0].split(' ')
        num = policy[0].split('-')
        first = int(num[0])
        second = int(num[1])
        char = policy[1]
        password = parts[1]
        check = 0
        if password[first - 1] == char:
            check += 1
        if password[second - 1] == char:
            check += 1
        if check == 1:
            valid += 1
    return valid


if __name__ == '__main__':
    # print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
