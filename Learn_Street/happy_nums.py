'''Happy number is defined by following process:'''
'''1) Starting with any positive integer, replace the number by the sum of the squares of its digits, and'''
'''2) Repeat the process until the number equals 1 (where it will stay).'''
'''If not, it loops endlessly in a cycle which does not include 1 (unhappy number!).'''
'''REPLACE THIS CODE WITH YOUR happynum METHOD'''

#Happy Numbers Project
def happynum(num):
	sum = 0
	a = str(num)
	while sum != 1:
		sum = 0
		for numbr in a:
			integer = (int(numbr))**2
			sum = integer + sum
		a = str(sum)
		print(sum)

	
if __name__ == "__main__":
	happynum(input("Insert an integer here: "))