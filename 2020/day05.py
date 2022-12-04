# -*- coding: utf-8 -*-
import utils

input = utils.get_input_multiline_str(5)


# input = '''BFFFBBFRRR
# FFFBBBFRRR
# BBFFBBFRLL'''.split('\n')


def find_seat_id(ticket):
    first = ticket[0:7]
    second = ticket[7:10]
    list_row = list(range(0, 128))
    list_col = list(range(0, 8))
    pos_first = 128
    pos_second = 8
    row = 0
    col = 0
    for i in first:
        pos_first = pos_first // 2
        if i == 'F':
            list_row = list_row[0:pos_first]
        else:
            list_row = list_row[pos_first:]

        if len(list_row) == 1:
            row = list_row[0]
            break

    for i in second:
        pos_second = pos_second // 2
        if i == 'L':
            list_col = list_col[0:pos_second]
        else:
            list_col = list_col[pos_second:]

        if len(list_col) == 1:
            col = list_col[0]
            break
    return row * 8 + col


def first():
    largest = 0
    for ticket in input:
        tid = find_seat_id(ticket)
        print(tid)
        if tid >= largest:
            largest = tid
    return largest


def second():
    seats = []
    for ticket in input:
        seats.append(find_seat_id(ticket))
    seats.sort()
    for i in range(0, len(seats) - 2):
        if seats[i + 1] > seats[i] + 1:
            print(seats[i], seats[i+1])
            break


if __name__ == '__main__':
    #find_seat_id('BFFFBBFRRR')
    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
