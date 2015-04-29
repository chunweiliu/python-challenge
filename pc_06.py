"""
http://www.pythonchallenge.com/pc/def/channel.html

title: now there are pairs
[A picture of zip named channel.jpg]
"""

# should be something related to the zip function
# zip what?
# visised zip.html
# -> yes. find the zip.

# load the image to local -> nothing you can do with an image
# ! changed the html to zip
# (http://jenstander.com/2011/01/16/learning-python-with-the-python-challenge-levels-0-6/)

import urllib
import os
import zipfile

URL = 'http://www.pythonchallenge.com/pc/def/channel.html'
ZIP_FILE = 'channel.zip'


def download_zip():
    url = URL.replace(os.path.basename(URL), ZIP_FILE)
    urllib.urlretrieve(url, ZIP_FILE)


def browse_zip():
    with zipfile.ZipFile(ZIP_FILE) as f:
        # print f.namelist()  # there is a readme.txt in the zip

        print f.read('readme.txt')  # in the zip, see a file name readme.txt
        # "welcome to my zipped list.
        # hint 1: start from 90052.txt
        # hint 2: answer is inside the zip"

        print f.read('90052.txt')  # "Next nothing is 94191"

        nothing = '94191'
        done = False
        while not done:
            line = f.read(nothing + '.txt')
            print line

            nothing = line.split()[-1]
            if nothing.isdigit() is False:
                # "Collect the comments."
                # No idea what's this utill Google it.
                done = True


def collect_comments():
    comments = list()
    with zipfile.ZipFile(ZIP_FILE) as f:
        nothing = '90052'
        done = False
        while not done:
            name = nothing + '.txt'
            line = f.read(name)
            comments += f.getinfo(name).comment

            nothing = line.split()[-1]
            if nothing.isdigit() is False:
                done = True
    return comments


def approach():
    """
    My approach to the solution
    """
    download_zip()
    # browse_zip()
    comments = collect_comments()
    os.remove(ZIP_FILE)

    print ''.join(comments)
    # the word HOCKEY is composed by small character oxygen
    ans = URL.replace(os.path.basename(URL), 'oxygen.html')
    print ans

if __name__ == '__main__':
    approach()
