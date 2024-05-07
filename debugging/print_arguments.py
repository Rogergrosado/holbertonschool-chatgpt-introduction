#!/usr/bin/python3
# The above line is called a shebang. It tells the system which interpreter to use to execute this script.

import sys  # Importing the sys module which provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.

# Iterating over each command-line argument passed to the script.
for i in range(1, len(sys.argv)):
    # Printing each command-line argument.
    print(sys.argv[i])

