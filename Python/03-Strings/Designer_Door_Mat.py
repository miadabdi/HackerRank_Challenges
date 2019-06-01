# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = list(map(int, input().split()))
multiple = 1
for index in range(1, n + 1):
    if index <= int(n / 2):
        symbol = '.|.' * multiple
        print(symbol.center(m, '-'))
        multiple += 2
    elif index == n // 2 + 1:
        print('WELCOME'.center(m, '-'))
    elif index > n // 2 + 1:
        multiple -= 2
        symbol = '.|.' * multiple
        print(symbol.center(m, '-'))
