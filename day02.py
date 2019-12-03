# -*- coding: utf-8 -*-
import utils
import math
from functools import reduce

input = utils.get_input_oneline_int(2)


# input = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]


def first():
    input[1] = 12
    input[2] = 2
    return get_output(input.copy())


def second():
    for i in range(0, 100):
        for j in range(0, 100):
            input[1] = i
            input[2] = j
            try:
                if get_output(input.copy()) == 19690720:
                    return 100 * i + j
            except IndexError:
                continue


def get_output(input):
    for i in range(0, len(input), 4):
        p = input[i:i + 4]
        if p[0] == 1:
            input[p[3]] = input[p[1]] + input[p[2]]
        elif p[0] == 2:
            input[p[3]] = input[p[1]] * input[p[2]]
        elif p[0] == 99:
            break
    return input[0]


if __name__ == '__main__':
    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
