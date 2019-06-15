# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = list(map(int, input().split()))
marks = []
for _ in range(x):
    marks.append(list(map(float ,input().split())))
marks = zip(*marks)
for avg_num in marks:
    print(sum(avg_num) / len(avg_num))

