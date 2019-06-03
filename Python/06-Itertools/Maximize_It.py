# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
k, m = list(map(int, input().split()))

lists = [list(map(int, input().split()))[1:] for _ in range(k)]

max_obtained = 0
possibles = list(product(*lists))
for possible in possibles:
    if max_obtained < (sum([num ** 2 for num in possible]) % m):
        max_obtained = (sum([num ** 2 for num in possible]) % m)

print(max_obtained)
