# Enter your code here. Read input from STDIN. Print output to STDOUT
from re import compile
for _ in range(int(input())):
    try:
        compile(input())
        print(True)
    except:
        print(False)
