# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
NO_shoes = int(input())
shoes_sizes = dict(Counter(list(map(int, input().split()))))
eared = 0
for _ in range(int(input())):
    shoe_size, price = list(map(int, input().split()))
    if shoe_size in shoes_sizes:
        if shoes_sizes[shoe_size] > 0:
            shoes_sizes[shoe_size] -= 1
            eared += price
print(eared)
