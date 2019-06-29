import numpy

numpy.set_printoptions(legacy='1.13')

n, m = map(int, input(). split())

A = [list(map(int, input().split())) for _ in range(n)]

print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
print(numpy.std(A, axis=None))
