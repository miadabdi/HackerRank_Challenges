# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k = int(input())
rooms = list(map(int, input().split()))
rooms = Counter(rooms)
print(sorted(rooms, key=lambda x: rooms[x])[0])
