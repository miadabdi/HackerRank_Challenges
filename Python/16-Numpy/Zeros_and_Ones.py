import numpy

a = list(map(int, input().split()))

result = numpy.zeros(a, dtype=numpy.int)
print(result)

result = numpy.ones(a, dtype=numpy.int)
print(result)
