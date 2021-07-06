#! /usr/bin/env python
import sys

#1 따로따로 처리하는 과정

try: 
    num = int(input("Enter: "))
except ValueError as err1:
    print(err1)
    sys.exit()

try:
    print(10/num)
except ZeroDivisionError as err:
    print(err)
    sys.exit()


#2 except을 한 번에 처리

try:
    num = int(input("Enter: ")
    print(10/num)
except ZeroDivisionError as err:
    print(err)
    sys.exit()
except ValueError as err1:
    print(err1)
    sys.exit()


