#Peter wants to generate some prime numbers for his cryptosystem. Help him!
#Your task is to generate all prime numbers between two given numbers!

#Input
#The input begins with the number t of test cases in a single line (t<=10). In each 
#of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000)
#separated by a space.

#Output
#For every test case print all prime numbers p such that m <= p <= n, one number per line, 
#test cases separated by an empty line.

def primeFinder(a,b):
	count=0
	if a>b:
		x=b
		for number in range(b,a):
			for x in range(1,number):
				if number/x == 1  or number/x == number:
					count=count+1
					if count==1:
						count=0
						return number
					else:
						count=0
					
				
	elif b>a:
		x=a
		for number in range(a,b):
			for x in range(1,number):
				if number/x == 1 or number/x == number:
					count=count+1
					if count==1:
						count=0
						return number
					else:	
						count=0
	else:
		return 0

if __name__=="__main__":		
	print primeFinder(1,10)
		