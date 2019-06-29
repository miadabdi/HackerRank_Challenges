import numpy
n, m, p = map(int, input().split())

first_array = [list(map(int, input().split())) for _ in range(n)]
second_array = [list(map(int, input().split())) for _ in range(n)]

result = numpy.concatenate((first_array, second_array), axis=0)

print(result)