#Given an array containing only stars '*' and hashes '#' . Find longest contiguous sub array that
#will contain equal no. of stars '*' and hashes '#'. Order (n) solution required.

lister=['#','#','#','*','*','#','#','#','*','*','*','#','#','#','#','*']
counter1=0
counter2=0
pos = 0
new_list1=[]
new_list2=[]
cur_max=0

lister.append('x')
for x in lister:
	if lister[pos]=='#':
		while lister[pos] == '#':
			counter1=counter1+1
			if pos <len(lister):
				if lister[pos+1] != '#':
					new_list1.append(counter1)
					counter1=0
				pos=pos+1
				print pos

	if lister[pos]=='*':
		while lister[pos] == '*':
			counter2=counter2+1
			if pos <len(lister):
				if lister[pos+1] != '*':
					new_list2.append(counter2)
					counter2=0
				pos=pos+1
				print pos
				

for x in new_list1:
	for y in new_list2:
		if x+y>cur_max:
			cur_max=x+y
			max_nl1=x
			max_nl2=y
print cur_max, max_nl1,max_nl2
		
	



print new_list1
print new_list2
	