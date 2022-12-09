# -*- coding: utf-8 -*-
import utils

input = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''

# input = '''R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20'''

input = utils.get_input(9)

input = utils.get_multiline_str(input)


def is_adjecent(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1


def move_tail(head, tail, markers, add_marker=True):
    if not is_adjecent(head, tail):
        delta_y = head[0] - tail[0]
        delta_x = head[1] - tail[1]
        if delta_y == 0:
            if delta_x > 0: tail[1] += 1
            else: tail[1] -= 1

        elif delta_x == 0:
            if delta_y > 0: tail[0] += 1
            else: tail[0] -= 1
        else:
            if delta_y > 0: tail[0] += 1
            else: tail[0] -= 1

            if delta_x > 0: tail[1] += 1
            else: tail[1] -= 1
        add_marker and markers.add(str(tail))


def first():
    head = [0, 0]
    tail = [0, 0]
    markers = set()
    markers.add(str(tail))
    for line in input:
        direction, steps = line.split(' ')
        steps = int(steps)
        for i in range(0, steps):
            if direction == 'R':
                head[1] += 1
            elif direction == 'L':
                head[1] -= 1
            elif direction == 'U':
                head[0] += 1
            elif direction == 'D':
                head[0] -= 1
            move_tail(head, tail, markers)
    return len(markers)


def second():
    ropes = [[0, 0] for i in range(0, 10)]
    markers = set()
    markers.add(str([0, 0]))
    for line in input:
        direction, steps = line.split(' ')
        steps = int(steps)
        for i in range(0, steps):
            if direction == 'R':
                ropes[0][1] += 1
            elif direction == 'L':
                ropes[0][1] -= 1
            elif direction == 'U':
                ropes[0][0] += 1
            elif direction == 'D':
                ropes[0][0] -= 1

            for j in range(0, 9):
                move_tail(ropes[j], ropes[j + 1], markers, j == 8)

    return len(markers)


if __name__ == '__main__':
    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
