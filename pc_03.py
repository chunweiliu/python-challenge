"""
http://www.pythonchallenge.com/pc/def/equality.html

One small letter, surrounded by EXACTLY three big bodyguards
on each of its sides.
"""

import urllib2
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

# View the page source and find the patten using regular expression.
expression = '[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]'  # EXACTLY 3 big
matches = list()
for line in urllib2.urlopen(url):
    matches += re.findall(expression, line)

# The answer is the combination of the small letters in the pattern.
small_letters = ''.join([match[len(match)/2] for match in matches])

# Replace the base name of the url by the result we got above.
ans = url.replace(url.split('/')[-1].split('.')[0], small_letters)
ans = ans.replace('html', 'php')  # Figure this out after visiting the html
print ans
