"""
http://www.pythonchallenge.com/pc/def/0.html

                38
An image with 2

Hint: try to change the URL address.
"""
base = 'http://www.pythonchallenge.com/pc/def/0.html'
key = 2 ** 38
url = base.replace('0', str(key))
print url
