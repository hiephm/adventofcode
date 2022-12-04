# -*- coding: utf-8 -*-
import utils

input = utils.get_input(6)


# input = '''abc
#
# a
# b
# c
#
# ab
# ac
#
# a
# a
# a
# a
#
# b'''


def first():
    total = 0
    for group in input.split('\n\n'):
        answers = []
        for person in group:
            for a in person.strip():
                answers.append(a)
        uniq = list(dict.fromkeys(answers))
        print(uniq)
        total += len(uniq)
    return total


def second():
    total = 0
    for group in input.split('\n\n'):
        answers = set(list('abcdefghijklmnopqrstuvwxyz'))
        for person in group.split('\n'):
            answers = answers & set(list(person.strip()))
        total += len(answers)
    return total


if __name__ == '__main__':

    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
