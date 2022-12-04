# -*- coding: utf-8 -*-
import utils

input = '''A Y
B X
C Z'''

input = utils.get_input(2)

input = utils.get_multiline_str(input)

scores1 = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3,  # Scissors

    'X': 1,  # Rock
    'Y': 2,  # Paper
    'Z': 3,  # Scissors
}

scores2 = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3,  # Scissors

    'X': 0,  # Lose
    'Y': 3,  # Draw
    'Z': 6,  # Win
}


def get_score1(op, your):
    result = scores1[your] - scores1[op]
    score1 = scores1[your]
    score2 = 0
    if result == 0:  # draw
        score2 = 3
    elif result == 1 or result == -2:
        score2 = 6
    return score1 + score2


def get_score2(op, result):
    score1 = scores2[result]
    if result == 'Y':
        score2 = scores2[op]
    elif result == 'Z':
        score2 = 1 if op == 'C' else scores2[op] + 1
    else:
        score2 = 3 if op == 'A' else scores2[op] - 1
    return score1 + score2


def first():
    total_score = 0
    for line in input:
        r = line.split(' ')
        total_score += get_score1(r[0], r[1])

    return total_score


def second():
    total_score = 0
    for line in input:
        r = line.split(' ')
        total_score += get_score2(r[0], r[1])

    return total_score


if __name__ == '__main__':
    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
