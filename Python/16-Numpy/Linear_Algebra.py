import numpy

n = int(input())
A = [list(map(float, input().split())) for _ in range(n)]

# result = float("{0:.2f}".format(numpy.linalg.det(A)))
result = round(numpy.linalg.det(A), 2)
print(result)
