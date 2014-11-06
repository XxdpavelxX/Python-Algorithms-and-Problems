__author__ = 'xxdpavelxx'
#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

#string_bits('Hello') = 'Hlo'
#string_bits('Hi') = 'H'
#string_bits('Heeololeo') = 'Hello'

def string_bits(str):
    x=0
    list=[]
    for char in str:
        if x%2==0:
            list.append(char)
        x=x+1
    ans=''.join(list)
    return ans

if __name__=="__main__":
    print string_bits('Hello')
    print string_bits('Hi')
    print string_bits('Heeololeo')