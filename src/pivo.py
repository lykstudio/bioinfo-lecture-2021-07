# 숫자를 넣으면 인덱스가 되어 그것에 해당하는 숫자 돌려주는 피보나치 수열 만들기

import sys

def pivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pivo(n-2) + pivo(n-1)

n = int(sys.argv[1])
print(pivo(n))


