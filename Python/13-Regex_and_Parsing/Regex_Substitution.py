# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def change(match):
    if match.group(1) == '||':return ' or'
    elif match.group(1) == '&&':return ' and'
for _ in range(int(input())):
    string = re.sub(r'\s(\|\||&&)(?=(\s))', change, input())
    print(string)
