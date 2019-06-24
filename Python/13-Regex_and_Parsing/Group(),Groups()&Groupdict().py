# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def occurrence(s):
    m = re.findall(r'([\da-z](?=([\da-z])))', s)
    for item in m:
        if item[0] == item[1]:
            return item[0]
    return -1

print(occurrence(input()))
