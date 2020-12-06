# -*- coding: utf-8 -*-
import utils
import math
from functools import reduce

input = utils.get_input_multiline_int(1)
#input = [100756]


def first():
    result = reduce(lambda x, y: x + y, map(lambda x: math.floor(x / 3) - 2, input))
    return result


def second():
    result = reduce(lambda x, y: x + y, map(cal_full_mass, input))
    return result


def cal_full_mass(x):
    total = 0
    mass = math.floor(x / 3) - 2
    while mass > 0:
        total += mass
        mass = math.floor(mass / 3) - 2
    return total


if __name__ == '__main__':
    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
