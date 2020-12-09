# -*- coding: utf-8 -*-
import utils

input = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''

input = utils.get_input(9)

input = utils.get_multiline_int(input)


def find_sum(number, num_list):
    for i in range(0, len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == number:
                return True
    return False


def first(preamble=5):
    for i in range(0, len(input)):
        if not find_sum(input[preamble + i], input[i:i+preamble]):
            return input[preamble + i]
    return ''


def second():
    first_result = first(25)
    for i in range(2, len(input)):
        for j in range(0, len(input) - i - 1):
            if sum(input[j:j+i]) == first_result:
                return max(input[j:j+i]) + min(input[j:j+i])
    return ''


if __name__ == '__main__':

    print('First: {}'.format(first(25)))
    print('Second: {}'.format(second()))
