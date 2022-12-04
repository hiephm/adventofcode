# -*- coding: utf-8 -*-
import utils

input = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

input = utils.get_input(11) # type: list

input = utils.get_multiline_str(input)


def count_occupied(input, i, j):
    occupied = 0
    for i1 in range(i-1, i+2):
        for j1 in range(j-1, j+2):
            if i1 == i and j1 == j:
                continue
            if input[i1][j1] == '#':
                occupied += 1
    return occupied

row_count = len(input)
row_len = len(input[0])


def count_occupied2(input, i, j):
    marked = [0] * 8
    occupied = []
    for d in range(1, 100):
        plot = {
            0: (i-d, j-d),
            1: (i-d, j),
            2: (i-d, j+d),
            3: (i, j-d),
            4: (i, j+d),
            5: (i+d, j-d),
            6: (i+d, j),
            7: (i+d, j+d),
        }

        if i - d < 0: # no above row:
            marked[0] = marked[1] = marked[2] = 1
        if i + d >= row_count:
            marked[5] = marked[6] = marked[7] = 1
        if j - d < 0:
            marked[0] = marked[3] = marked[5] = 1
        if j + d >= row_len:
            marked[2] = marked[4] = marked[7] = 1

        for pos, coordinate in plot.items():
            if marked[pos] == 0 and input[coordinate[0]][coordinate[1]] != '.':
                marked[pos] = 1
                occupied.append(input[coordinate[0]][coordinate[1]])
        if marked.count(1) == 8:
            return occupied.count('#')
    return 0


def flip_seat(input, i, j):
    l = list(input[i])
    if l[j] == '#':
        l[j] = 'L'
    elif l[j] == 'L':
        l[j] = '#'
    input[i] = ''.join(l)


def is_same_pattern(p1, p2):
    return ''.join(p1) == ''.join(p2)


def first():
    global input
    row_len = len(input[0])
    input.insert(0, ''.join(['.'] * row_len))
    input.append(''.join(['.'] * row_len))
    for i in range(0, len(input)):
        input[i] = '.' + input[i] + '.'

    row_count = len(input)
    row_len = len(input[0])

    while True:
        cloned = list(input)
        for i in range(1, row_count):
            for j in range(1, row_len):
                if input[i][j] == '.':
                    continue
                elif (input[i][j] == 'L' and count_occupied(input, i, j) == 0) or \
                     (input[i][j] == '#' and count_occupied(input, i, j) >= 4):
                    flip_seat(cloned, i, j)
        if is_same_pattern(cloned, input):
            break
        else:
            input = cloned

    for row in cloned:
        print(row)
    return ''.join(cloned).count('#')


def second():
    global input
    while True:
        cloned = list(input)
        for i in range(0, row_count):
            for j in range(0, row_len):
                if input[i][j] == '.':
                    continue
                elif (input[i][j] == 'L' and count_occupied2(input, i, j) == 0) or \
                        (input[i][j] == '#' and count_occupied2(input, i, j) >= 5):
                    flip_seat(cloned, i, j)
        if is_same_pattern(cloned, input):
            break
        else:
            input = cloned
    return ''.join(cloned).count('#')

if __name__ == '__main__':

    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
