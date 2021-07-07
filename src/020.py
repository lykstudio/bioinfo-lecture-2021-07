#! /usr/bin/env python

# 내가 작성한 답안
#import sys

#a = sys.argv[1]
#b = sys.argv[2]
#c = a + b
#print(c)
#띄어쓰기
#print(a + " " + b)
#print(f"{a} {b}")

#강사님 풀이

#var1 = "Bio"
#var2 = "Informatics"
#var3 = var1 + var2
#print(var3)



# 클래스 이용
class A:
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        return self.val + other.val
   
    def __mul__(self, other):
        return "__mul__"
    def __len__(self):
        return 0

a1 = A("a")
a2 = A("b")
print(a1.val + a2.val)
print(a1 + a2)
print(a1*a2)
print(len(a1))





