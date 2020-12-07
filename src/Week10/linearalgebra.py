import numpy

size_of_array = int(input())
array = []
for _ in range(size_of_array):
    array.append(list(map(float, input().split())))

result = numpy.linalg.det(array)
print(round(result, 2))

