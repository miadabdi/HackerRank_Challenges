# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
n_set = set(list(map(int, input().split())))
b = int(input())
b_set = set(list(map(int, input().split())))

print(len(n_set.union(b_set)))
