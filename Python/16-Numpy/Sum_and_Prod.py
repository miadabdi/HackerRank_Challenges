import numpy

n, m = map(int, input().split())

arrays = [list(map(int, input().split())) for _ in range(n)]

my_array = numpy.array(arrays)

sum_array = numpy.sum(my_array, axis=0)
print(numpy.prod(sum_array, axis=0))
