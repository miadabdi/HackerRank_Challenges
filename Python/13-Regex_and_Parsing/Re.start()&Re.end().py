# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s, k = input(), input()
matches = [match.span(1) for match in re.finditer(r'(?=(%s))' % k, s)]
if len(matches):
    for match in matches:
        start, end = match
        print((start, end - 1))
else: print((-1, -1))
