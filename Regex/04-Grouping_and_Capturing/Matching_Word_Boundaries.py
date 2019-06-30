from string import ascii_letters

Regex_Pattern = r'\b[aeiouAEIOU][%s]*\b' % ascii_letters	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())