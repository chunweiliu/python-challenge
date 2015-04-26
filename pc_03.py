"""
http://www.pythonchallenge.com/pc/def/equality.html

One small letter, surrounded by EXACTLY three big bodyguards
on each of its sides.
"""

import urllib2
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

expression = '[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]'  # EXACTLY 3 big
matches = list()
for line in urllib2.urlopen(url):
    matches += re.findall(expression, line)
small_letters = ''.join([match[len(match)/2] for match in matches])

# replace the base name of the url by the result we got above
ans = url.replace(url.split('/')[-1].split('.')[0], small_letters)
ans = ans.replace('html', 'php')
print ans
