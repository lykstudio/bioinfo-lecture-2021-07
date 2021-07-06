#! /usr/bin/env python

import sys

try:
    with open("hahaha.txt", 'r') as handle:
        data = handle.readlines()
except FileNotFoundError as err:
    prin("파일이 없음")
    sys.exit()

print(data)
