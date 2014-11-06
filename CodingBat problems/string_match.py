__author__ = 'xxdpavelxx'

#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz"
# and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

#string_match('xxcaazz', 'xxbaaz') = 3
#string_match('abc', 'abc') = 2
#string_match('abc', 'axc') = 0

def string_match(a, b):
    x=0
    y=2
    count=0
    while y<=len(a):
        if a[x:y]==b[x:y]:
            count=count+1
        x=x+1
        y=y+1
    return count


if __name__ =="__main__":
    print string_match('xxcaazz', 'xxbaaz')
    print string_match('abc', 'abc')
    print string_match('abc', 'axc')