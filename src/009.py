#! /usr/bin/env python


def greet():
    print("Hell, Bioinformatics")

def greet1(name: str) -> None:
    print(f"Hello, {name}")

def greet2(num: int) -> int:
    return num*2

greet()
greet1("ken")
print(greet2(3))



