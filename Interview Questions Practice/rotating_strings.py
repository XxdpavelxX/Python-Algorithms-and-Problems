#1.8 Assume you have a method isSubstring which checks if one word is a substring of
#another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using 
#only one call to isSubstring  'waterbottle' is a rotation of 'erbottlewat'.

#simple solution
def isSubstring(s1,s2):
	big_string=s1+s1
	if s2 in big_string:
		return "String %s is a rotation of sring %s" %(s1,s2)
	else:
		return "Strings are not a rotation of each other"



if __name__=="__main__":
	print isSubstring("waterbottle","erbottlewat")