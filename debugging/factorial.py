#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) < 2:
    print("Please provide a number as a command line argument")
else:
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError as e:
        print(e)
