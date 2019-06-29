import numpy

n, m = map(int, input().split())

arrays = [list(map(int, input().split())) for _ in range(n)]

my_array = numpy.array(arrays)

print(numpy.max(numpy.min(my_array, axis=1)))

