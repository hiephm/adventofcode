# -*- coding: utf-8 -*-
import utils
import re
input = utils.get_input_multiline_str(7)


input = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.split('\n')


def first():
    allbags = {}
    for line in input:
        result = re.match('^(.*) bags contain (\d+ .* bag[s]?)\.$', line)
        if result:
            parent = result.group(1)
            allbags[parent] = []
            children = result.group(2).split(', ')
            for child in children:
                result = re.match('^\d+ (.*) bag[s]?$', child)
                if result:
                    allbags[parent].append(result.group(1))

    shiny_gold_parents = ['shiny gold']
    while True:
        cloned = list(allbags.items())
        old_len = len(cloned)
        for parent, children in cloned:
            for p in shiny_gold_parents:
                if p in children:
                    shiny_gold_parents.append(parent)
                    if allbags.get(parent):
                        del allbags[parent]
        # print(shiny_gold_parents)
        print(old_len, len(allbags.items()))
        if old_len == len(allbags.items()):
            break
    print('====', len(set(shiny_gold_parents)) - 1)
    # print(len(set(shiny_gold_parents)))
    # print(allbags)

allbags = {}
for line in input:
    result = re.match('^(.*) bags contain (\d+ .* bag[s]?)\.$', line)
    if result:
        parent = result.group(1)
        allbags[parent] = []
        children = result.group(2).split(', ')
        for child in children:
            result = re.match('^(\d+) (.*) bag[s]?$', child)
            if result:
                allbags[parent].append((int(result.group(1)), result.group(2)))

def second(child):
    total = 0
    children = allbags.get(child)
    if not children:
        return 1
    for c, b in children:
        print(c, b)
        total += c * second(b)
        print(total)
    return total



if __name__ == '__main__':
    #print('First: {}'.format(first()))
    print('Second: {}'.format(second('shiny gold')))
