# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
c = divmod(a, b)
print("{}\n{}\n{}".format(c[0], c[1], c))
