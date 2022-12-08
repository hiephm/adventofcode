# -*- coding: utf-8 -*-
import utils

input = '''30373
25512
65332
33549
35390'''

input = utils.get_input(8)

input = utils.get_multiline_str(input)

rows = len(input)
cols = len(input[0])
marker = [[0 for i in range(0, cols)] for j in range(0, rows)]


def first():
    for i in range(1, rows - 1):
        # consider from left to right:
        tallest = input[i][0]
        for j in range(1, cols - 1):
            if int(input[i][j]) > int(tallest):
                tallest = input[i][j]
                marker[i][j] = 1

        # consider from right to left:
        tallest = input[i][cols - 1]
        for j in range(cols - 2, 0, -1):
            if int(input[i][j]) > int(tallest):
                tallest = input[i][j]
                marker[i][j] = 1

    for j in range(1, cols - 1):
        # consider from up to down:
        tallest = input[0][j]
        for i in range(1, rows - 1):
            if int(input[i][j]) > int(tallest):
                tallest = input[i][j]
                marker[i][j] = 1

        # consider from down to up:
        tallest = input[rows - 1][j]
        for i in range(rows - 2, 0, -1):
            if int(input[i][j]) > int(tallest):
                tallest = input[i][j]
                marker[i][j] = 1

    visible_trees = 2*rows + 2*(cols - 2)
    for row in marker:
        visible_trees += sum(row)

    return visible_trees


def second():
    max_view_score = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if marker[i][j] == 1:
                view_score = 1

                # look left:
                count_tree = 0
                for x in range(1, j+1):
                    count_tree += 1
                    if input[i][j] <= input[i][j-x]:
                        break
                view_score *= count_tree

                # look right:
                count_tree = 0
                for x in range(j+1, cols):
                    count_tree += 1
                    if input[i][j] <= input[i][x]:
                        break
                view_score *= count_tree

                # look up:
                count_tree = 0
                for x in range(1, i+1):
                    count_tree += 1
                    if input[i][j] <= input[i-x][j]:
                        break
                view_score *= count_tree

                # look down:
                count_tree = 0
                for x in range(i+1, rows):
                    count_tree += 1
                    if input[i][j] <= input[x][j]:
                        break
                view_score *= count_tree

                if view_score > max_view_score:
                    max_view_score = view_score

    return max_view_score


def pretty_print(arr):
    for line in arr:
        print(line)


if __name__ == '__main__':
    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
