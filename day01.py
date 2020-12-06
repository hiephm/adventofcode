# -*- coding: utf-8 -*-
import utils

input = utils.get_input_multiline_int(1)


# input = sample input


def first():
    for i in range(0, len(input)):
        for j in range(i, len(input)):
            if input[i] + input[j] == 2020:
                print(input[i], input[j], input[i] * input[j])


def second():
    for i in range(0, len(input)):
        for j in range(i, len(input)):
            for k in range(j, len(input)):
                if input[i] + input[j] + input[k] == 2020:
                    print(input[i], input[j], input[k], input[i] * input[j] * input[k])


if __name__ == '__main__':
    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
