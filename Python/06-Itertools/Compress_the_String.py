# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s = input()
for character, occure in groupby(s):
    print("({}, {}) ".format(len(list(occure)), character), end="")
