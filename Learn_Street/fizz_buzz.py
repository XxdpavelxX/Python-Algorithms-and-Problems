"""program that prints number from 1-100 but for multiples of 3 print fizz instead of number but for multiple 5 print buzz, and for 
multiple of 3 and 4 print fizz buzz."""

#for x in range(1,100):
#	if x %3 ==0 and x%5 == 0:
#		print ("fizz buzz")
#	if x % 3 == 0: 
#		print ("fizz")
#	elif x % 5 == 0:
#		print ("buzz")
#	else:
#		print (x)
	
		
""" Use list comprehension to make a list of even numbers in range 10"""
#print (list(range(0,10,2)))
	
#print (list(number for number in range(0,10) if number % 2))

rows = range(1,4)
cols = range(1,3)
#print (list((row,col) for row in rows for col in cols))
cells = [(row,col) for row in rows for col in cols]
#for cell in cells:
#	print (cell)
#for row, col in cells:
#	print (row,col)

#word = 'letters'
#letter_counts = {letter:word.count(letter) for letter in word}
#print (letter_counts)

 #odd_set = {number for number in range(1,6) if number %2
 
 #Tuples do not have comprehensions!!!
 
 #generator:
 number thing = (number for number in range(1,6))
 for number in number_thing:
	print (number)
	
	
#to make generator into list:
number_list = list(number_thing)
number_list
# Important! A generator can only be run once!. Lists, sets, string and dictionaries are saved in memory but generators are not. They create values on the fly and do not remember them!

#Cannot reeiterate same generator
try_again = list(number_thing)
>>> try_again
>>> []