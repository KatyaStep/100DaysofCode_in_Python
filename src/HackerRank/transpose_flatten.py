import numpy

# n, m = map(int, input().split())
# my_array = []
# for i in range(n):
#     my_array.append(list(map(int, input().split())))
#
# print(numpy.transpose(numpy.array(my_array)))
# print(numpy.array(my_array).flatten())

# import numpy
#
# my_array = list(map(int, input().split()))
# change_arr = numpy.array(my_array)
#
# print(numpy.reshape(change_arr, (3, 3)))

import numpy



n, m, p = list(map(int, input().split()))
array1 = []
array2 = []
for _ in range(n):
    array1.append(list(map(int, input().split())))

for _ in range(m):
    array2.append(list(map(int, input().split())))


print(numpy.concatenate((numpy.array(array1), numpy.array(array2))))
#print(array1, array2)