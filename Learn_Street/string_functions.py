#Ready to start the string_functions-python project? 
#Read the Overview content on the left and click the Start button 
#when you are ready to begin the project.
r_str = 0
def revers(str):
	list = []
	length = len(str)
	for x in range(len(str)):
		#print (str[length-1])
		list.append(str[length-1])
		if length !=0:
			length = length -1
	global r_str
	r_str = ''.join(list)
	print (r_str)

def uppercase(str):
	print (str.upper())

def palindrome(str):
	if r_str == str:
		print ("is a palindrome")
	else:
		print ("is not a palindrome")
if __name__ == "__main__":
	a = input("Insert a string here: ")
	revers(a)
	uppercase(a)
	palindrome(a)
	
