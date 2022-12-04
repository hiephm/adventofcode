# -*- coding: utf-8 -*-
import utils

input = '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''

input = utils.get_input(1)

#input = utils.get_multiline_str(input)

def first():
    groups = input.split('\n\n')
    max = 0
    for group in groups:
        int_group = list(int(i) if i else 0 for i in group.split('\n'))
        if sum(int_group) > max:
            max = sum(int_group)
    return max


def second():
    groups = input.split('\n\n')
    list_sum = []
    for group in groups:
        int_group = list(int(i) if i else 0 for i in group.split('\n'))
        list_sum.append(sum(int_group))
    list_sum = sorted(list_sum, reverse=True)
    return sum(list_sum[0:3])


if __name__ == '__main__':

    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
