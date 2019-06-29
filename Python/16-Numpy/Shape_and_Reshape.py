import numpy

arr = list(map(int, input().split()))

numArr = numpy.array(arr)
print(numpy.reshape(numArr, (3, 3)))

