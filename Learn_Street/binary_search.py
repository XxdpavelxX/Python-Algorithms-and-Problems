def binarySearch(arr, val):
	lo = 0
	hi = len(arr)-1
	ctr = 0
	mid = int((lo + hi)/2)
	current = arr[mid]
	arr.sort()   #sort values into numerical order in case they aren't already


		
	while val != arr[mid]:
		if val > arr[mid]:
			ctr = ctr + 1
			print (arr[mid])
			mid = int((mid + hi)/2)
			if val<arr[mid] and val>arr[mid-1]:    #do this if value is in between to table values.
				print ("Value not in table")
			if val>arr[-2]:    #so we can test if value is last number in array
				if val == arr[-1]:
					mid=-1
				else:
					print ("Value not in table")
				
				
			
			
		if val < arr[mid]:
			ctr = ctr +1
			print (arr[mid])
			mid = int((mid +lo)/2)
			if val<arr[mid] and val>arr[mid-1]:    #do this if value is in between to table values but not in table.
				print ("Value not in table")
			if val<arr[1]:    #so we can test if value is first number in array
				if val == arr[0]:
					mid = 0
				else:
					print ("Value not in table")

	if val == arr[mid]:
		ctr = ctr + 1
		print (arr[mid])
		print (mid, ctr)   #returns value on list and how many tries it took to find

		
		

binarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13],3)