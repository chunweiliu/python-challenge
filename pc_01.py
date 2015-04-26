"""
http://www.pythonchallenge.com/pc/def/map.html

K -> M
O -> Q
E -> G

everybody thinks twice before solving this.

g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle
   gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle
     qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""


def char_shift(string, padding):
    """
    Shift the charters in the string right with the padding number
    @ param (str) string
    @ param (int) padding
    @ return (str) the shifted string
    """
    alphabets = ''.join(map(lambda x: str(unichr(x+ord('a'))), range(26)))
    shifted = [alphabets[(alphabets.find(char) + padding) % 26]
               if alphabets.find(char) > -1 else char  # avoid punctuations
               for char in string]
    return ''.join(shifted)

url = 'http://www.pythonchallenge.com/pc/def/map.html'
string = """
    g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
    bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
    sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

print ' '.join([char_shift(word, 2) for word in string.split()])

ans = url.replace('map', char_shift('map', 2))
print ans
