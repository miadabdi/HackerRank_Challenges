import math
import os
import random
import re
import sys

# Complete the solve function below.


import string

def solve(s):
    s_new = ''
    for index in range(len(s)):
        if index == 0:
            s_new += s[index].upper()
        elif s[index - 1] == ' ':
            s_new += s[index].upper()
        else:
            s_new += s[index]
    return s_new


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
