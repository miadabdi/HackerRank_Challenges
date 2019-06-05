# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = list(map(int, input().split()))
groups = defaultdict(list)
for _ in range(n):
    groups['group_A'].append(input())
for _ in range(m):
    groups['group_B'].append(input())

for hey, given_item in enumerate(list(groups.items())[1][1]):
    if given_item not in list(groups.items())[0][1]:
        print("-1")
    else:
        for index, item in enumerate(list(groups.items())[0][1]):
            if given_item == item:
                print(index + 1, end="")
                print(" ", end="")
        print()
        