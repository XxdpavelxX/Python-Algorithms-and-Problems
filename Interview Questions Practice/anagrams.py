#1.4 Write a method to decide if two strings are anagrams or not.

def anagrams(string1,string2):
	a_string1= sorted(string1)
	a_string2= sorted(string2)
	if a_string1==a_string2:
		return "%s and %s are anagrams of each other" %(string1,string2)
	else:
		return "%s and %s are not anagrams" %(string1,string2)

if __name__=="__main__":		
	print anagrams("hellvo", "olxhel")