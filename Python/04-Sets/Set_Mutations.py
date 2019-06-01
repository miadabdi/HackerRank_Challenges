# Enter your code here. Read input from STDIN. Print output to STDOUT
len_elements = int(input())
A_elements = set(map(int, input().split()))
for _ in range(int(input())):
    eval("A_elements.{0}({1})".format(input().split()[0], list(map(int, input().split()))))
print(sum(A_elements))
