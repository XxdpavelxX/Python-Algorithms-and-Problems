#1.3 Design an algorithm and write code to remove the duplicate characters in a string
#without using any additional buffer. NOTE: One or two additional variables are fine.
#An extra copy of the array is not.


#solution 1  Better solution
def duplicate_remover(string):
	unique_chars=[]
	for char in string:
		if char not in unique_chars:
			unique_chars.append(char)
	unique_string=('').join(unique_chars)
	return unique_string
	
	
#solution 2
def duplicate_remover2(string):
	unique_chars=set()
	for char in string:
		unique_chars.update(char)
	return unique_chars

if __name__=="__main__":
	print duplicate_remover('Hello my name is Pavel')