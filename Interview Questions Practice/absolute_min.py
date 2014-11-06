#Given three arrays A,B,C containing unsorted numbers. Find three numbers a, b, c from each of array A, B, C such that |a-b|,
#|b-c| and |c-a| are minimum Please provide as efficient code as you can. Can you better than this ???
list1 = [1,3,5,4,9]
list2 = [0,8,7,6,2]
list3= [12,3,9,6,15]

def finder(listy1,listy2,listy3):
	listy1.sort()
	listy2.sort()
	listy3.sort()
	min=999999999999999

	for a in listy1:
		for b in listy2:
			for c in listy3:			
				if abs(a-b)+abs(b-c)+abs(c-a) < min:
					min = abs(a-b)+abs(b-c)+abs(c-a)
					x1=a
					x2=b
					x3=c
				
	print min, x1,x2,x3
	
finder(list1,list2,list3)
				