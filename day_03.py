# -*- coding: utf-8 -*-
import utils

input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

input = utils.get_input(3)

input = utils.get_multiline_str(input)

def first():
    total = 0
    for line in input:
        part1 = line[0:len(line)//2]
        part2 = line[len(line)//2:]
        item = next(iter(set(part1).intersection(set(part2))))
        if item.islower():
            total += ord(item) - ord('a') + 1
        else:
            total += ord(item) - ord('A') + 27
    return total


def second():
    total = 0
    for i in range(0, len(input), 3):
        part1 = input[i]
        part2 = input[i + 1]
        part3 = input[i + 2]
        item = next(iter(set(part1).intersection(set(part2)).intersection(set(part3))))
        if item.islower():
            total += ord(item) - ord('a') + 1
        else:
            total += ord(item) - ord('A') + 27



    return total


if __name__ == '__main__':

    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
