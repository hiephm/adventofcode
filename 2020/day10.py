# -*- coding: utf-8 -*-
import utils

input = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''


input = utils.get_input(10)

input = utils.get_multiline_int(input)

input.append(0)
input.append(max(input) + 3)
input.sort()
print(input)


def first():
    last_adapter = 0
    dist = {}
    for i in input:
        diff = i - last_adapter
        dist[diff] = dist[diff] + 1 if dist.get(diff) else 1
        last_adapter = i
    print(dist[1] * dist[3])
    return dist


def second():
    travelled = {0: 1}
    for i in range(1, len(input)):
        current = input[i]
        previous_1 = input[i - 1]
        travelled[current] = travelled[previous_1]
        if i >= 2 and current - input[i - 2] <= 3:
            travelled[current] += travelled[input[i - 2]]
        if i >= 3 and current - input[i - 3] <= 3:
            travelled[current] += travelled[input[i - 3]]

    print(travelled)
    return ''


if __name__ == '__main__':

    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
