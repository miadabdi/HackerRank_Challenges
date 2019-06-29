import numpy

n, m = map(int, input().split())

A, B = [list(map(int, input().split())) for _ in range(n)], [list(map(int, input().split())) for _ in range(n)]

A, B = numpy.array(A), numpy.array(B)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
