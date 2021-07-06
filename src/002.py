#! /usr/bin/env python

# try1

r = 3
pi = 3.14

circle = pi*r**2
print(circle)


# try2


import math
import sys


if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()


r = int(sys.argv[1])
pi = math.pi
result = round(r**2*pi, 2)

print(result)

