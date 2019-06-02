# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase
z = complex(input())
print((z.real ** 2 + z.imag ** 2) ** 0.5)
print(phase(z))
