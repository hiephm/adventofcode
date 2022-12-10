# -*- coding: utf-8 -*-
import utils

input = ''''''

input = utils.get_input(10)

input = utils.get_multiline_str(input)


def tick(cycle, x, store):
    cycle += 1
    if cycle in (20, 60, 100, 140, 180, 220):
        store.append(cycle * x)
    return cycle


def first():
    cycle = 0
    x = 1
    store = []
    for line in input:
        parts = line.split(' ')
        if parts[0] == 'noop':
            cycle = tick(cycle, x, store)
        elif parts[0] == 'addx':
            cycle = tick(cycle, x, store)
            cycle = tick(cycle, x, store)
            x += int(parts[1])

    return sum(store)


def tick2(cycle, x, store):
    pos = cycle % 40
    if pos == 0:
        store.append(['.'] * 40)
    if x - 1 <= pos <= x + 1:
        store[len(store) - 1][pos] = '#'
    return cycle + 1


def second():
    cycle = 0
    x = 1
    store = []
    for line in input:
        parts = line.split(' ')
        if parts[0] == 'noop':
            cycle = tick2(cycle, x, store)
        elif parts[0] == 'addx':
            cycle = tick2(cycle, x, store)
            cycle = tick2(cycle, x, store)
            x += int(parts[1])

    utils.pretty_print(store)

    return ''


if __name__ == '__main__':
    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
