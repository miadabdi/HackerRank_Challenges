# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    HEX = '0123456789ABCDEFabcdef'
    matches = re.findall(r'[^\^]\s?#([%s]{6}|[%s]{3})[^\w$]' % (HEX, HEX), input())
    for match in matches:
        print('#' + match)
