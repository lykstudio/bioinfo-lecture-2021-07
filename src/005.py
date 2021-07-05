#! /usr/bin/env python

import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

num1 = int(sys.argv[1])

if num1 % 3 == 0:
    print("3의 배수")

elif num1 % 7 == 0:
    print("7의 배수")

else:
    print("3의 배수도 7의 배수도 아님")




# 강사님 작성 방법

import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [n1]")
    sys.exit()


n1 = int(sys.argv[1])

if n1 % 3 == 0 and n1 % 7 == 0:
    result = "3, 7"
elif n1 % 3 == 0:
    result = "3"
elif n1 % 7 == 0:
    result = "7"

print(result)

