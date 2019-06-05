# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
order = input().split()
print(sum([int(list(input().split())[order.index('MARKS')]) for _ in range(n)]) / n)
