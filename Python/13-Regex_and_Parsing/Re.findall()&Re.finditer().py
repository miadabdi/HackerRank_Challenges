# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
vowels = 'AEIOUaeiou'
regex = r'[%s]([%s]{2,})(?=[%s])' % (consonants, vowels, consonants)
matches = re.findall(regex, input())
if len(matches): [print(match) for match in matches]
else: print(-1)
