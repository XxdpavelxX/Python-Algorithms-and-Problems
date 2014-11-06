#1.5 Write a method to replace all spaces in a string with percent20.
#solution 1
def replacer(string):
	replaced_list=[]
	for char in string:
		if char==" ":
			replaced_list.append("%20")
		else:
			replaced_list.append(char)
	replaced_list="".join(replaced_list)
	return replaced_list
	
#solution2 (use regular expressions)
#solution3 (use python replace command)
		
		
if __name__=="__main__":
	print replacer("hello david")
	#string.replace(" ","%20")