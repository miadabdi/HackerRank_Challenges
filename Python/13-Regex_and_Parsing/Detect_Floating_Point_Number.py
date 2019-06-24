# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    regex = r'^[+-.]{0,1}\d*\.\d+$'
    print(re.search(regex, input()) != None)
