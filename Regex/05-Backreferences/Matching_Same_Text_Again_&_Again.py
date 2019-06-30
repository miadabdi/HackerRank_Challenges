from string import ascii_letters, ascii_lowercase, ascii_uppercase

vowels = 'aeiouAEIOU'
Regex_Pattern = r'^([%s])(\w)(\s)(\W)(\d)(\D)([%s])([%s])([%s])(\S)\1\2\3\4\5\6\7\8\9\10$' % (ascii_lowercase, ascii_uppercase, ascii_letters, vowels)	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())