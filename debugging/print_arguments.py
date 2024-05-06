#!/usr/bin/python3
"""
I changed the start of the loop from index 1,
instead of index 0, to skip the 1st arg.
"""
import sys

for i in range(1, len(sys.argv)):
    print(sys.argv[i])
