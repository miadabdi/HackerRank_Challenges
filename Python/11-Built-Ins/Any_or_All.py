# Enter your code here. Read input from STDIN. Print output to STDOUT

n, n_integers = int(input()), list(map(int, input().split()))
print(all([True if num > 0 else False for num in n_integers]) and any([True if str(num) == str(num)[::-1] else False for num in n_integers]))
