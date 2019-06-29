import numpy

numpy.set_printoptions(legacy='1.13')

n = int(input())

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

print(numpy.dot(A, B))
