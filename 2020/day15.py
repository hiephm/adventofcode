# -*- coding: utf-8 -*-
import utils
from datetime import datetime

input = '''1,20,8,12,0,14'''
#input = '''0,3,6'''

input = utils.get_oneline_int(input)


def first():
    global input
    seen = {}
    spoken = 0
    start = datetime.now()
    for turn in range(1, 2021):
        if len(input) > 0:
            spoken = input[0]
            input = input[1:]
        else:
            seen_turns = seen.get(spoken)
            if len(seen_turns) == 1:
                spoken = 0
            else:
                spoken = seen_turns[-1] - seen_turns[-2]
        if seen.get(spoken):
            seen[spoken].append(turn)
            if len(seen[spoken]) > 2:
                seen[spoken] = seen[spoken][1:]
        else:
            seen[spoken] = [turn]
        print('Turn {}: {}'.format(turn, spoken))
    print('Time taken: {}'.format(datetime.now() - start))
    return spoken


def second():
    global input
    seen = {}
    for turn in range(1, len(input)):
        seen[input[turn-1]] = turn
        print('Turn {}: {}'.format(turn, input[turn-1]))

    spoken = input[-1]
    for turn in range(len(input), 30000000):
        if turn % 1000000 == 0:
            print('Turn {}: {}'.format(turn, spoken))
        seen_last = seen.get(spoken)
        seen[spoken] = turn
        if seen_last:
            spoken = turn - seen_last
        else:
            spoken = 0
    return spoken


if __name__ == '__main__':

    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
