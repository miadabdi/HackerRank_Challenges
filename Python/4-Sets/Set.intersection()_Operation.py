# Enter your code here. Read input from STDIN. Print output to STDOUT
English_sub_total = int(input())
English_subs = set(map(int, input().split()))
French_sub_total = int(input())
French_subs = set(map(int, input().split()))

print(len(English_subs.intersection(French_subs)))
