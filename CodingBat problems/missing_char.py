__author__ = 'xxdpavelxx'


#Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string
#(i.e. n will be in the range 0..len(str)-1 inclusive).

#missing_char('kitten', 1) = 'ktten'
#missing_char('kitten', 0) = 'itten'
#missing_char('kitten', 4) = 'kittn'

def missing_char(str, n):
    list_chars=[]
    for char in str:
        list_chars.append(char)
    list_chars.remove(list_chars[n])
    result = ''.join(list_chars)
    return result


if __name__ =="__main__":
    print missing_char('kitten',1)
    print missing_char('kitten', 0)
    print missing_char('kitten', 4)
