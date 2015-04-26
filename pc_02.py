"""
http://www.pythonchallenge.com/pc/def/ocr.html

recognize the characters. maybe they are in the book,
but MAYBE they are in the page source.
"""

import urllib2

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

rare_characters = []
for i, line in enumerate(urllib2.urlopen(url)):
    if i > 37:  # start to find the rare characters
        rare_characters += [char if char.isalpha() else '' for char in line]
rare_characters = ''.join(rare_characters)

ans = url.replace('ocr', rare_characters)
print ans
