# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
supersub = True
for _ in range(int(input())):
    other = set(map(int, input().split()))
    if other.intersection(a) != other:
        supersub = False
    else:
        if len(a) <= len(other):
            supersub = False
print(supersub)
