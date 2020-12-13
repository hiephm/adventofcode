# -*- coding: utf-8 -*-
import utils

input = '''939
1789,37,47,1889'''

input = utils.get_input(13)

input = utils.get_multiline_str(input)

timestamp = int(input[0])
bus_schedule = input[1].split(',')
avail_bus = []
for bus in bus_schedule:
    if bus != 'x':
        avail_bus.append(int(bus))


def first():
    global timestamp
    wait_time = 0
    while True:
        for bus in avail_bus:
            if timestamp % bus == 0:
                return wait_time * bus
        timestamp += 1
        wait_time += 1


def second():
    avail_bus = []
    pos = 0
    for bus in bus_schedule:
        if bus != 'x':
            avail_bus.append((pos, int(bus)))
        pos += 1
    print(avail_bus)
    step = avail_bus[0][1]
    start = avail_bus[0][1]
    loop = 0
    for i in range(1, len(avail_bus)):
        multiply = 1
        while True:
            loop += 1
            t = step * multiply
            if (start + t + avail_bus[i][0]) % avail_bus[i][1] == 0:
                print('=====', start + t)
                start = start + t
                step *= avail_bus[i][1]
                break
            else:
                multiply += 1
        print(start, step, loop)




if __name__ == '__main__':

    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
