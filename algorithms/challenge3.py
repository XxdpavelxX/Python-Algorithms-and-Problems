#__author__ = 'xxdpavelxx'
#import re

#text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
# sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

#first= re.sub('k','m', text)
#second=re.sub('o','q', first)
#third=re.sub('e','g', second)
#print third


import sys
inputText = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw
fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
lmu ynnjw ml rfc spj."""

inputText2= 'http://www.pythonchallenge.com/pc/def/map.html'

SHIFTAMOUNT = 2
for char in inputText2:
#don't convert these
    if char in ("."," ",",","'","(",")"):
        print char,
        continue
#move text on as per map
    ascii = ord(char)
    ascii += SHIFTAMOUNT
#if moved past end of alphabet then go back to start

    if ascii > ord('z'):

        ascii -= 26
    #print chr(ascii),   this produces unwanted spaces, so....
    sys.stdout.write(chr(ascii))
print inputText2