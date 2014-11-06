#Write a method which will remove any given character from a target string.  Don't use the String.replace() method in your solution.
#'If the given character is not found in the target string, your method should raise a CharacterNotFound exception

import re
from math import sqrt
def remover(char,string):
    try:
        num=string.find(char)
        sqrt(num)
        ans = re.sub(char,'',string)
        return ans

    except:
        raise Exception ("CharacterNotFound exception")

    #word_list = string.split(' ')
    #for word in word_list:
     #   if char in word:
      #      word.delete(char)
    #print word_list

if __name__ == '__main__':
    print remover('b',"Hello there you cool man")