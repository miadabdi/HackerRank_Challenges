# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    a, a_set = int(input()), set(map(int, input().split()))
    b, b_set = int(input()), set(map(int, input().split()))
    if a_set.intersection(b_set) == a_set:
        print(True)
    else:
        print(False)
