# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, string
from email.utils import parseaddr, formataddr
for _ in range(int(input())):
    name, mail = parseaddr(input())
    arguments = (string.ascii_letters, string.ascii_letters, string.ascii_letters)
    pattern = r'^[%s][-\w.]+@[%s]{2,}\.[%s]{1,3}$' % arguments
    if re.search(pattern, mail) != None:
        print(formataddr((name, mail)))
