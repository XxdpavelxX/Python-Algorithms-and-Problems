__author__ = 'xxdpavelxx'
#Given a non-empty string like "Code" return a string like "CCoCodCode".

#string_splosion('Code') = 'CCoCodCode'
#string_splosion('abc') = 'aababc'
#string_splosion('ab') = 'aab'

def string_splosion(str):
    text=[str[0]]
    y=2
    while y<len(str)+1:
        text.append(str[:y])
        y=y+1
    ans= ''.join(text)
    return ans


    #if len(str)<3:
     #   return str[0]+str
    #elif len(str)==3:
     #   return str[0]+str[:2]+str[:3]
    #elif len(str)==4:
     #   return str[0]+str[:2]+str[:3]+str[:4]
if __name__=="__main__":
    print string_splosion('Code')
    print string_splosion('abc')
    print string_splosion('ab')


