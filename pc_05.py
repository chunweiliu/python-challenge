"""
http://www.pythonchallenge.com/pc/def/peak.html

pronounce it
"""

# View page source and found
# <!-- peak hell sounds familiar ? -->
# -> pickle


import cPickle
import urllib2

url = 'http://www.pythonchallenge.com/pc/def/banner.p'  # found in the source
string = urllib2.urlopen(url).read()  # read the romote pickle file in raw
data = cPickle.loads(string)  # parse the raw data in to serialized data

# How to use the data? No idea: found a hint here:
# https://teacode.wordpress.com/2013/06/26/level-5-pickle/
for line in data:
    print ''.join(elmt[0] * elmt[1] for elmt in line)

# The result showed in console was "channel" (not obvious in the REPL console)
ans = url.replace('banner.p', 'channel.html')
print ans
