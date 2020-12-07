from cmath import phase

z = 1+2j
f = phase(z)
r = abs(z)
print('{:0.3f}'.format(r))
print('{:0.3f}'.format(f))

