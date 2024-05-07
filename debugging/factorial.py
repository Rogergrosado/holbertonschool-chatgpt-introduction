#!/usr/bin/python3

import sys

# Function to calculate the factorial of a given number
def factorial(n):
    result = 1
    # Loop through each number from n down to 1
    while n > 1:
        # Multiply the result by the current value of n
        result *= n
        # Decrement n for the next iteration
        n = n - 1
    # Return the final result
    return result

# Get the input from the command-line arguments and calculate factorial
f = factorial(int(sys.argv[1]))

# Print the factorial
print(f)

