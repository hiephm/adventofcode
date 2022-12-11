# -*- coding: utf-8 -*-
import utils
import re

input = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''

input = utils.get_input(11)


def parse_monkeys():
    monkeys = []

    for block in input.split('\n\n'):
        lines = block.split('\n')
        monkey = {
            'items'        : re.findall('\d+', lines[1]),
            'op'           : lines[2].split(' = ')[1],
            'test'         : int(re.findall('\d+', lines[3])[0]),
            'test_true'    : int(lines[4][-1]),
            'test_false'   : int(lines[5][-1]),
            'inspect_count': 0
        }
        monkeys.append(monkey)
    return monkeys


def first():
    monkeys = parse_monkeys()

    for round in range(0, 20):
        for monkey in monkeys:
            items = monkey['items']
            while len(items) > 0:
                monkey['inspect_count'] += 1
                item = items[0]
                monkey['items'] = items[1:]
                items = monkey['items']
                old = int(item)
                worry_level = eval(monkey['op']) // 3
                if worry_level % monkey['test'] == 0:
                    monkeys[monkey['test_true']]['items'].append(worry_level)
                else:
                    monkeys[monkey['test_false']]['items'].append(worry_level)

    monkeys = sorted(monkeys, key=lambda x: x['inspect_count'], reverse=True)

    utils.print_list(monkeys)

    return monkeys[0]['inspect_count'] * monkeys[1]['inspect_count']


def second():
    monkeys = parse_monkeys()
    dividers = [d['test'] for d in monkeys]
    print(dividers)

    for round in range(0, 10000):
        for index, monkey in enumerate(monkeys):
            items = monkey['items']
            while len(items) > 0:
                monkey['inspect_count'] += 1
                item = items[0]
                monkey['items'] = items[1:]
                items = monkey['items']

                if isinstance(item, str):
                    remainders = []
                    for d in dividers:
                        old = int(item)
                        worry_level = eval(monkey['op'])
                        remainders.append(worry_level % d)
                    item = remainders
                else:
                    for i in range(0, len(item)):
                        old = item[i]
                        worry_level = eval(monkey['op'])
                        item[i] = worry_level % dividers[i]
                if item[index] == 0:
                    monkeys[monkey['test_true']]['items'].append(item)
                else:
                    monkeys[monkey['test_false']]['items'].append(item)

    monkeys = sorted(monkeys, key=lambda x: x['inspect_count'], reverse=True)

    utils.print_list(monkeys)

    return monkeys[0]['inspect_count'] * monkeys[1]['inspect_count']


if __name__ == '__main__':
    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
