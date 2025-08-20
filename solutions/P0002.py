#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def __fibo_helper(n, a=1, b=1):
    if(n <= 0): 
        return n
    if n == 1:
        return b
    return __fibo_helper(n-1, b, a+b)

def fibonacci(n=10):
    return __fibo_helper(n)

def compute():
    sum = 0
    n = 1
    term = 1
    while(True): 
        term = fibonacci(n)
        if term > 4000000:
            break;
        if term % 2 == 0:
            sum += term
        n += 1
    return sum

def main():
    print(compute())

if __name__ =="__main__":
    main() 