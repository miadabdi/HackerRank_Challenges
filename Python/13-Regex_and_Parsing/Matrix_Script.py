import math
import os
import random
import re
import sys

n, m = map(int, input().rstrip().split())
matrix = ['' for _ in range(m)]
for _ in range(n):
    for index, character in enumerate(input()):
        matrix[index] += character
matrix = ''.join(matrix)

print(re.sub(r'(\w+)\W+(?=\w+)' ,'\g<1> ' ,matrix))
