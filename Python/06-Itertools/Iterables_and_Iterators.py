# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n = int(input())
letters = input().split()
combs = list(combinations(letters, int(input())))
aCount = [item for item in combs if 'a' in item]
print(len(aCount) / len(combs))
