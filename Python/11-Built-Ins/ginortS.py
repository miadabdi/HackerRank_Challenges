# Enter your code here. Read input from STDIN. Print output to STDOUT
from string import ascii_lowercase, ascii_uppercase
s = input()

lower, upper, odd, even = [], [], [], []

for character in s:
    if character in ascii_lowercase: lower.append(character)
    elif character in ascii_uppercase: upper.append(character)
    elif int(character) % 2 == 0: even.append(character)
    else: odd.append(character)

sortedS = ''.join(sorted(lower))
sortedS += ''.join(sorted(upper))
sortedS += ''.join(sorted(odd))
sortedS += ''.join(sorted(even))

print(sortedS)
