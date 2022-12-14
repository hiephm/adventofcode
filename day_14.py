# -*- coding: utf-8 -*-
import utils

input = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''

input = utils.get_input(14)

input = utils.get_multiline_str(input)


def build_cave_map():
    cave_map = [['.']*800 for i in range(0, 200)]
    cave_depth = 0
    for line in input:
        points = line.split(' -> ')
        for i in range(0, len(points) - 1):
            x1, y1 = (int(v) for v in points[i].split(','))
            x2, y2 = (int(v) for v in points[i+1].split(','))
            if x1 == x2:
                if y1 > y2:
                    y1, y2 = y2, y1
                for j in range(y1, y2 + 1):
                    cave_map[j][x1] = '#'
            else:
                if x1 > x2:
                    x1, x2 = x2, x1
                for j in range(x1, x2 + 1):
                    cave_map[y1][j] = '#'
            if y1 > cave_depth:
                cave_depth = y1
            if y2 > cave_depth:
                cave_depth = y2

    return cave_map, cave_depth


def first():
    cave_map, cave_depth = build_cave_map()
    cave_map[0][500] = '+'
    all_rest = False
    sand_count = 0
    while not all_rest:
        sand_pos = [0, 500]
        for i in range(0, cave_depth + 1):
            if sand_pos[0] == cave_depth:
                all_rest = True
                break

            under = cave_map[i + 1][sand_pos[1]]
            left = cave_map[i + 1][sand_pos[1] - 1]
            right = cave_map[i + 1][sand_pos[1] + 1]
            # check under
            if under == '.':
                sand_pos[0] += 1
                continue
            elif left == '.':
                sand_pos[0] += 1
                sand_pos[1] -= 1
                continue
            elif right == '.':
                sand_pos[0] += 1
                sand_pos[1] += 1
                continue
            else:
                cave_map[sand_pos[0]][sand_pos[1]] = 'o'
                sand_count += 1
                break

    #utils.pretty_print(cave_map)

    return sand_count


def second():
    cave_map, cave_depth = build_cave_map()
    cave_depth += 2
    for i in range(0, len(cave_map[0])):
        cave_map[cave_depth][i] = '#'
    cave_map[0][500] = '+'
    all_rest = False
    sand_count = 0
    while not all_rest:
        sand_pos = [0, 500]
        for i in range(0, cave_depth + 1):
            under = cave_map[i + 1][sand_pos[1]]
            left = cave_map[i + 1][sand_pos[1] - 1]
            right = cave_map[i + 1][sand_pos[1] + 1]
            # check under
            if under == '.':
                sand_pos[0] += 1
                continue
            elif left == '.':
                sand_pos[0] += 1
                sand_pos[1] -= 1
                continue
            elif right == '.':
                sand_pos[0] += 1
                sand_pos[1] += 1
                continue
            else:
                cave_map[sand_pos[0]][sand_pos[1]] = 'o'
                sand_count += 1
                if sand_pos[0] == 0:
                    all_rest = True
                break

    #utils.pretty_print(cave_map)

    return sand_count


if __name__ == '__main__':

    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
