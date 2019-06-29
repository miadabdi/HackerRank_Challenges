import numpy

numpy.set_printoptions(sign=' ')

n, m = map(int, input().split())

result = numpy.eye(n, m)

print(result)
