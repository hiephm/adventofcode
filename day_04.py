# -*- coding: utf-8 -*-
import utils

input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

input = utils.get_input(4)

input = utils.get_multiline_str(input)

def first():
    count = 0
    for line in input:
        first = line.split(',')[0]
        second = line.split(',')[1]
        first1 = int(first.split('-')[0])
        first2 = int(first.split('-')[1])
        second1 = int(second.split('-')[0])
        second2 = int(second.split('-')[1])
        if (first1 <= second1 and first2 >= second2) or (first1 >= second1 and first2 <= second2):
            count += 1
    return count


def second():
    count = 0
    for line in input:
        first = line.split(',')[0]
        second = line.split(',')[1]
        first1 = int(first.split('-')[0])
        first2 = int(first.split('-')[1])
        second1 = int(second.split('-')[0])
        second2 = int(second.split('-')[1])
        if (first1 <= second1 <= first2) or (first1 <= second2 <= first2) \
                or (second1 <= first1 <= second2) or (second1 <= first2 <= second2):
            count += 1
    return count


if __name__ == '__main__':

    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
