# Enter your code here. Read input from STDIN. Print output to STDOUT

m, m_values = int(input()), set(map(int, input().split()))
n, n_values = int(input()), set(map(int, input().split()))

diff = []
diff.extend(m_values.difference(n_values))
diff.extend(n_values.difference(m_values))
for item in sorted(diff):
    print(item)
