# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
word, r = input().split()
r = int(r)
for permute in permutations(sorted(word), r):
    print(''.join(permute))
