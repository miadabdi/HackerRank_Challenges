# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'append':
        d.append(int(command[1]))
    elif command[0] == 'appendleft':
        d.appendleft(int(command[1]))
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()

[print(str(item) + ' ', end="") for item in d]
