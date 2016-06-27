# -*- coding: utf-8 -*-

def fib(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a + b
        print a

fib(5)