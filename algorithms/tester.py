import re
from math import sqrt
def tester(input_list):
    list2=[]
    list3=[]

    for char in input_list:     #This loop converts all numbers into character format, and removes any letters in list
        if str(char).isdigit():
            list2.append(str(char))
    #return list2

    for value in list2:     #This makes sure that only duplicated numbers are listed, and that each of them is only listed once.
        if list2.count(value)>1:
            if value not in list3:
                list3.append(value)
    return list3


print tester(['a',1,2,1,'c',1,2,'d','d','3','3','3',1,3,'a',5,'a','b'])