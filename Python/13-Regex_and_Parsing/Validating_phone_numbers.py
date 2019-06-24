# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def is_valid(phoneNumber):
    if re.search(r"^[987]\d{9}$", phoneNumber) is not None:
        return 'YES'
    else:
        return 'NO'

for _ in range(int(input())):
    print(is_valid(input()))
