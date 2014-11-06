__author__ = 'xxdpavelxx'
#Given a string, return a new string where the first and last chars have been exchanged.

#front_back('code') = 'eodc'
#front_back('a') = 'a'
#front_back('ab') = 'ba'

def front_back(str):
    if len(str)>1:
        first=str[0]
        last=str[-1]
        rest=str[1:-1]
        return last+rest+first
    else:
        return str

if __name__=="__main__":
    print front_back('code')
    print front_back('a')
    print front_back('ab')