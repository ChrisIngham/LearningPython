
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('My number is 416-967-1111.')
print('Phone number found: ' + mo.group())