# -*- coding: utf-8 -*-
import utils

input = '''F10
N3
F7
R90
F11'''

input = utils.get_input(12)

input = utils.get_multiline_str(input)


def first():
    direction = ((0, 1), (1, -1), (0, -1), (1, 1))  # E / S / W / N
    current_dir = 0  # 0: E, 1: S, 2: W, 3: N
    position = [0, 0]  # East / North
    for line in input:
        command = line[0]
        value = int(line[1:])
        if command == 'F':
            position[direction[current_dir][0]] += value * direction[current_dir][1]
        elif command == 'R':
            turn_value = (value // 90)
            current_dir += turn_value
            if current_dir > 3:
                current_dir = current_dir - 4
        elif command == 'L':
            turn_value = (value // 90)
            current_dir -= turn_value
            if current_dir < 0:
                current_dir = current_dir + 4
        elif command == 'E':
            position[0] += value
        elif command == 'W':
            position[0] -= value
        elif command == 'N':
            position[1] += value
        elif command == 'S':
            position[1] -= value
    print(position)
    return abs(position[0]) + abs(position[1])


def second():
    waypoint = complex(10, 1)
    position = complex(0, 0)
    for line in input:
        command = line[0]
        value = int(line[1:])
        if command == 'F':
            position += (waypoint * value)
        elif command == 'R':
            turn_value = value // 90
            waypoint *= complex(0, -1) ** turn_value
        elif command == 'L':
            turn_value = value // 90
            waypoint *= complex(0, 1) ** turn_value
        elif command == 'E':
            waypoint += complex(value, 0)
        elif command == 'W':
            waypoint -= complex(value, 0)
        elif command == 'N':
            waypoint += complex(0, value)
        elif command == 'S':
            waypoint -= complex(0, value)
        print(position, waypoint)
    print(waypoint)
    return abs(position.real) + abs(position.imag)


if __name__ == '__main__':

    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
