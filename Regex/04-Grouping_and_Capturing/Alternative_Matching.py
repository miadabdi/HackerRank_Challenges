from string import ascii_letters

Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[%s]+$' % ascii_letters	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())