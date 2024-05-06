#!/usr/bin/python3
import sys

# Function Description: This function calculates the factorial of a given number using recursion.
# Parameters: n - The number for which the factorial is to be calculated.
# Returns: The factorial of the number n.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the number from the command line argument, calculate its factorial and print the result.
f = factorial(int(sys.argv[1]))
print(f)
