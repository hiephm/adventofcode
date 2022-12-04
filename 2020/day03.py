# -*- coding: utf-8 -*-
import utils

input = utils.get_input_multiline_str(3)


# input = '''..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
# '''.split('\n')


def first(right=3, down=1):
    tree = 0
    x = 0
    width = len(input[0])
    for i in range(0, len(input), down):
        if len(input[i]) == 0:
            continue
        x += right
        y = i + down
        if y >= len(input):
            break
        if x >= width:
            x -= width
        if len(input[y]) == 0:
            break
        if input[y][x] == '#':
            tree += 1
    return tree


def second():
    return first(1, 1) * first(3, 1) * first(5, 1) * first(7, 1) * first(1, 2)


if __name__ == '__main__':
    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
