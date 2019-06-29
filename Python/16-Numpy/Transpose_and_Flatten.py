import numpy
n, m = map(int, input().split())

listOfArrays = [list(map(int, input().split())) for _ in range(n)]

numArr = numpy.array(listOfArrays)

print(numArr.transpose())
print(numArr.flatten())
