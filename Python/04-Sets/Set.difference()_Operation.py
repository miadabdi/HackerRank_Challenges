# Enter your code here. Read input from STDIN. Print output to STDOUT

e = int(input())
English = set(map(int, input().split()))
f = int(input())
French = set(map(int, input().split()))

print(len(English.difference(French)))
