# -*- coding: utf-8 -*-
import utils
from functools import cmp_to_key

input = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

input = utils.get_input(13)

input = input.split('\n\n')


def compare(p1, p2):
    p1_is_list = isinstance(p1, list)
    p2_is_list = isinstance(p2, list)

    if p1_is_list and p2_is_list:
        if len(p1) == 0 and len(p2) > 0:
            return 'Right'
        elif len(p2) == 0 and len(p1) > 0:
            return 'Wrong'

        # Both lists are not empty
        for i in range(0, len(p1)):
            # Recursively compare each item (include case where p1 size is equal p2)
            if i < len(p2):
                result = compare(p1[i], p2[i])
                if result:
                    return result
            # p1 is bigger than p2
            else:
                return 'Wrong'
        # if goes here then check if p2 is bigger than p1
        if len(p2) > len(p1):
            return 'Right'
    # both of packets are integer
    elif not p1_is_list and not p2_is_list:
        if p1 < p2:
            return 'Right'
        elif p1 > p2:
            return 'Wrong'
    # one of packet is integer, convert it to list
    else:
        if p1_is_list:
            result = compare(p1, [p2])
        elif p2_is_list:
            result = compare([p1], p2)
        if result:
            return result

    return None


def first():
    pair_index = 0
    sum_right_order = 0
    for pair in input:
        pair_index += 1
        p1 = eval(pair.split('\n')[0])
        p2 = eval(pair.split('\n')[1])
        result = compare(p1, p2)
        if result == 'Right':
            sum_right_order += pair_index
        # print(pair_index, result)
    return sum_right_order


def compare_fucntion(p1, p2):
    result = compare(p1, p2)
    if result == 'Right':
        return -1
    elif result == 'Wrong':
        return 1
    else:
        return 0


def second():
    packets = [[[2]], [[6]]]
    for pair in input:
        packets.append(eval(pair.split('\n')[0]))
        packets.append(eval(pair.split('\n')[1]))

    packets.sort(key=cmp_to_key(compare_fucntion))
    decoder_key = 1
    for index, p in enumerate(packets):
        if p == [[2]] or p == [[6]]:
            decoder_key *= (index + 1)

    return decoder_key


if __name__ == '__main__':
    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
