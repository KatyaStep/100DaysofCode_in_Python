import numpy


a = []
n, m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))

my_array = numpy.array(a)

print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))
print(numpy.std(my_array))
