def binary_search(list, item):
	low = 0
	high = len(list)-1
	x=0
	
	while low <= high:
		mid = (low + high)/2
		guess = list[mid]
		
		if guess == item:
			print "Found in %s tries" %x
			return mid
			
			
		if guess >= item:
			high = mid - 1
			x=x+1
			
		else:
			low = mid+1
			x=x+1
			
	return None
my_list = [1,3,5,7,9]
print binary_search(my_list,3) # => 1
print binary_search(my_list,-1)	# => None
print binary_search(my_list,1)