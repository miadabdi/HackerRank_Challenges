# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
one, two = list(input().split())
for limit in range(1, int(two) + 1):
    for i in combinations(sorted(one), limit):
        print(''.join(i))
