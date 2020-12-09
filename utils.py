# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
load_dotenv()

import requests


def get_input(day, to_lines=False):
    cache_file = 'data_{}.txt'.format(day)
    if os.path.isfile(cache_file):
        with open(cache_file, 'r') as f:
            raw = f.read()
    else:
        headers = {
            'Cookie': os.getenv('COOKIE')
        }
        resp = requests.get('https://adventofcode.com/2020/day/{}/input'.format(day), headers=headers)
        raw = resp.text.strip()
        with open(cache_file, 'w') as f:
            f.write(raw)
    if to_lines:
        return raw.split('\n')
    else:
        return raw


def get_multiline_int(input):
    return list(map(int, input.split('\n')))


def get_multiline_str(input):
    return input.split('\n')


def get_input_multiline_int(day):
    lines = get_input(day, True)
    return list(map(int, lines))


def get_input_multiline_str(day):
    lines = get_input(day, True)
    return lines


def get_input_oneline_int(day):
    items = get_input(day).split(',')
    return list(map(int, items))


if __name__ == '__main__':
    print(get_input(4))
