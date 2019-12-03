# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
load_dotenv()

import requests


def get_input(day, to_lines=False):
    headers = {
        'Cookie': os.getenv('COOKIE')
    }
    raw = requests.get('https://adventofcode.com/2019/day/{}/input'.format(day), headers=headers)
    if to_lines:
        return raw.text.strip().split('\n')
    else:
        return raw.text.strip()


def get_input_multiline_int(day):
    lines = get_input(day, True)
    return list(map(int, lines))


def get_input_oneline_int(day):
    items = get_input(day).split(',')
    return list(map(int, items))
