#!/usr/bin/python3
import sys

# Function Description: This function calculates the factorial of a given number using recursion.
# Parameters: n - The number for which the factorial is to be calculated.
# Returns: The factorial of the number n.
def factorial(n):
    # Base case: If n is 0, return 1 because 0! is defined as 1.
    if n == 0:
        return 1
    else:
        # Recursive case: Multiply n by the factorial of (n-1) to get the factorial of n.
        return n * factorial(n-1)

# Get the number from the command line argument, calculate its factorial and print the result.

# Extract the number from the command line argument and convert it to an integer.
# Note: sys.argv[0] is the script name itself, so we start from index 1 to get the first command line argument.
number = int(sys.argv[1])

# Calculate the factorial of the number using the factorial function.
f = factorial(number)

# Print the result.
print(f)

