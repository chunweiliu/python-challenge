"""
http://www.pythonchallenge.com/pc/def/linkedlist.php

<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never
end. 400 times is more than enough. -->
"""

# Clicked the image and got an URL
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# and the next nothing is 44827

import urllib


def get_request(url, values):
    """
    Send a GET request to a website and return the response
    @param (str) url. The URL for the request
    @param (dict) values. The dictionary of query-value pair
    """
    data = urllib.urlencode(values)  # encode the query to a string
    url = '?'.join([url, data])      # join the php url and the query
    response = urllib.urlopen(url)   # return the content after the query
    return response

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
query = {'nothing': '12345'}
for i in range(400):
    response = get_request(url, query)
    value = response.readline().split()[-1]  # the last word in the web

    print 'Round {0}: {1}'.format(i, value)
    if value.split('.')[-1] == 'html':  # stop when hit *.html
        break
    else:
        query['nothing'] = value

ans = url.replace(url.split('/')[-1], value)
print ans
