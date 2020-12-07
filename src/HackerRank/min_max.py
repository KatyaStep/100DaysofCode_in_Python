import numpy

# a = numpy.array(([[2, 5],
#                   [3, 7],
#                   [1, 3],
#                   [4, 0]]))

a = []
n, m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))

my_array = numpy.array(a)
minimum = numpy.min(my_array, axis=1)
#
print(numpy.max(minimum))