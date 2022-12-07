# -*- coding: utf-8 -*-
import utils

input = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''

#input = utils.get_input(6)


def first():
    for i in range(0, len(input) - 4):
        if len(set(input[i:i + 4])) == 4:
            return i + 4


def second():
    for i in range(0, len(input) - 14):
        if len(set(input[i:i + 14])) == 14:
            return i + 14


if __name__ == '__main__':
    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
