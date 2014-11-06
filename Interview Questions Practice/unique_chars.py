#1.1 Implement an algorithm to determine if a string has all unique characters. What if you
#can not use additional data structures?

#solution1: MORE EFFICIENT SOLUTION
def analyzer(string):
	list_chars=[]
	for char in string:
		if char not in list_chars:
			list_chars.append(char)
		else:
			return "Not all characters in string are unique character:'%s' repeats itself" %char
	return "All characters are unique"
	
#solution2:
def analyzer2(string):
	unique_chars = set()
	unsorted_list=[]
	for char in string:
		unique_chars.add(char)
		unsorted_list.append(char)
	unsorted_set=[]
	for char in unique_chars:
		unsorted_set.append(char)
	sorted_set=sorted(unsorted_set)
	unique_set_string=('').join(sorted_set)
	sorted_list= sorted(unsorted_list)
	unique_string=('').join(sorted_list)
	
	print unique_set_string
	print unique_string
	if unique_set_string==unique_string:
		return "All characters are unique"
	else:
		return "Not all characters are unique"
	
			
if __name__=="__main__":
	 print analyzer("abcdD")