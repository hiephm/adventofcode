# -*- coding: utf-8 -*-
import utils
import re

input = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''

input = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

input = utils.get_input(14)

input = utils.get_multiline_str(input)


def masking1(value, mask):
    mask_len = len(mask)
    value_bin = '{{:0>{}b}}'.format(mask_len).format(value)
    value_masked = list(value_bin)
    for i, bit in enumerate(mask):
        if bit != 'X':
            value_masked[i] = bit
    return int(''.join(value_masked), 2)


def first():
    mem_map = {}
    current_mask = ''
    for line in input:
        result = re.match('^mask = (.*)$', line)
        if result:
            current_mask = result.group(1)
            continue
        result = re.match('^mem\[(\d+)\] = (\d+)', line)
        if result:
            mem_addr = result.group(1)
            value = int(result.group(2))
            mem_map[mem_addr] = masking1(value, current_mask)
    return sum(mem_map.values())


def masking2(address, mask):
    address_bin = '{{:0>{}b}}'.format(len(mask)).format(address)
    address_masked = list(address_bin)
    for i, bit in enumerate(mask):
        if bit != '0':
            address_masked[i] = bit
    address_masked = ''.join(address_masked)
    float_addresses = [address_masked]
    float_bit_count = address_masked.count('X')
    for i in range(0, float_bit_count):
        new_addresses = []
        for addr in float_addresses:
            new_addresses.append(addr.replace('X', '0', 1))
            new_addresses.append(addr.replace('X', '1', 1))
        float_addresses = new_addresses
    return list(map(lambda x: int(x, 2), float_addresses))


def second():
    mem_map = {}
    current_mask = ''
    for line in input:
        result = re.match('^mask = (.*)$', line)
        if result:
            current_mask = result.group(1)
            continue
        result = re.match('^mem\[(\d+)\] = (\d+)', line)
        if result:
            mem_addr = int(result.group(1))
            value = int(result.group(2))
            float_addresses = masking2(mem_addr, current_mask)
            for addr in float_addresses:
                mem_map[addr] = value
    return sum(mem_map.values())


if __name__ == '__main__':

    #print('First: {}'.format(first()))
    print('Second: {}'.format(second()))
