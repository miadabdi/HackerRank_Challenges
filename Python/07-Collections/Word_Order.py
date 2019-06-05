# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
words = [input() for _ in range(int(input()))]
print(len(set(words)))
Counts = Counter(words) 
[print(str(item[1]) + ' ', end="") for item in Counts.items()]
