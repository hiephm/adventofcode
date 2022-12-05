# -*- coding: utf-8 -*-
import utils
import re

input = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

input = utils.get_input(5)


def parse_first_part(input):
    lines = input.split('\n')
    cols = {}
    for line in lines[:-1]:
        pos = 1
        for i in range(0, len(line), 4):
            box = line[i + 1:i + 2]
            if box != ' ':
                if cols.get(pos):
                    cols.get(pos).append(box)
                else:
                    cols[pos] = [box]
            pos += 1
    return cols


def first():
    parts = input.split('\n\n')
    cols = parse_first_part(parts[0])
    pattern = re.compile('move (\d+) from (\d+) to (\d+)')

    lines = parts[1].split('\n')
    for line in lines:
        steps = pattern.findall(line)[0]
        s1 = int(steps[0])
        s2 = int(steps[1])
        s3 = int(steps[2])
        for i in range(0, s1):
            cols[s3].insert(0, cols[s2].pop(0))
    result = ''
    for k, v in cols.items():
        result += v[0]
    return result


def second():
    parts = input.split('\n\n')
    cols = parse_first_part(parts[0])
    pattern = re.compile('move (\d+) from (\d+) to (\d+)')

    lines = parts[1].split('\n')
    for line in lines:
        steps = pattern.findall(line)[0]
        s1 = int(steps[0])
        s2 = int(steps[1])
        s3 = int(steps[2])
        cols[s3] = cols[s2][0:s1] + cols[s3]
        cols[s2] = cols[s2][s1:]
    result = ''
    for k, v in cols.items():
        result += v[0]
    return result


if __name__ == '__main__':
    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
