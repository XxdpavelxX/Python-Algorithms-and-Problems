__author__ = 'xxdpavelxx'
#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

#not_string('candy') = 'not candy'
#not_string('x') = 'not x'
#not_string('not bad') = 'not bad'

def not_string(str):
    not_list=[]
    list_words= str.split(' ')
    if list_words[0] !="not":
        not_list.append("not")
        for word in list_words:
            not_list.append(word)
        return ' '.join(not_list)
    else:
        return ' '.join(list_words)

if __name__=="__main__":
    print not_string('candy one')
    print not_string('candy')
    print not_string('x')
    print not_string('not bad')