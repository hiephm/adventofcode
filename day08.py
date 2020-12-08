# -*- coding: utf-8 -*-
import utils
import re

input = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split('\n')

input = utils.get_input_multiline_str(8)


def parse_cmd(line):
    result = re.match('(.+) ([\+\-]\d+)', line)
    if not result:
        print(line)
    return result.group(1), int(result.group(2))


def first(cmds):
    acc = 0
    run_steps = []
    current_step = 0
    while True:
        if current_step in run_steps:
            print(acc)
            return False

        if current_step >= len(cmds):
            return acc
        cmd = parse_cmd(cmds[current_step])
        run_steps.append(current_step)
        if cmd[0] == 'acc':
            acc += cmd[1]
            current_step += 1
        elif cmd[0] == 'nop':
            current_step += 1
        elif cmd[0] == 'jmp':
            current_step += cmd[1]


def second():
    start = 0
    while True:
        cloned = list(input)
        for i in range(start, len(input)):
            cmd = parse_cmd(cloned[i])
            if cmd[0] == 'nop':
                cloned[i] = cloned[i].replace('nop', 'jmp')
                break
            elif cmd[0] == 'jmp':
                cloned[i] = cloned[i].replace('jmp', 'nop')
                break

        result = first(cloned)
        if result:
            return result
        else:
            start = i + 1


if __name__ == '__main__':
    print('First: {}'.format(first(input)))
    # print('Second: {}'.format(second()))
