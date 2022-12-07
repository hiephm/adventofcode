# -*- coding: utf-8 -*-
import utils
import re

input = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

input = utils.get_input(7)

input = utils.get_multiline_str(input)

file_pattern = re.compile('(\d+) .*')
cd_pattern = re.compile('\$ cd (.*)')

dirs = {}


def first():
    stack = []
    for line in input:
        cd = cd_pattern.findall(line)
        files = file_pattern.findall(line)

        if cd:
            if cd[0] == '..':
                stack.pop()
            else:
                stack.append(cd[0])
                dirs['_'.join(stack)] = 0
        elif files:
            for i in range(1, len(stack) + 1):
                dirs['_'.join(stack[0:i])] += int(files[0])

    total_size = 0
    for _, size in dirs.items():
        if size <= 100000:
            total_size += size

    return total_size


def second():
    root_size = dirs['/']
    need_to_free = root_size - 40000000
    all_sizes = sorted(dirs.values())
    for size in all_sizes:
        if size > need_to_free:
            return size


if __name__ == '__main__':
    print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
