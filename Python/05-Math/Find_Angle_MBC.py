# Enter your code here. Read input from STDIN. Print output to STDOU
from math import acos, degrees
ab, bc = int(input()), int(input())
# Solution: https://en.wikipedia.org/wiki/Law_of_cosines
ac = (ab ** 2 + bc ** 2) ** 0.5
mc = ac / 2
cosine_of_the_angle = (((mc ** 2) + (bc ** 2)) - (mc ** 2)) / (2 * mc * bc)
print(str(round(degrees(acos(cosine_of_the_angle))))+'°')
