# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def is_valid(s):
    matches = list(re.finditer(r'^([456]\d{3})-?(\d{4})-?(\d{4})-?(\d{4})$', s))
    if len(matches):
        matches = ''.join(matches[0].groups())
        if re.search(r'(\d)\1\1\1' ,matches) == None:
            return 'Valid'
        else: return 'Invalid'
    return 'Invalid'

for _ in range(int(input())):
    print(is_valid(input()))
