#Write a function to find the nth "ugly number". ugly numbers are numbers that can only be fully divided by 1, 2, 3, 5 and itself.
def ugly_finder(n):
	x = 0
	number = 5
	
	if n % 1 != 0:
		raise Exception("Please only input integers greater than 0. Decimals of non-number characters will not be accepted")
	if n == 0:
		raise Exception("Please only input integers greater than 0. Decimals of non-number characters will not be accepted")


	while x <n:
		if number%3 ==0:
			if number%2== 0:
				x=x+1
				number = number +5
				if x == n:
					return number-5
			else:
				number = number + 5
		else:
			number = number +5
		
if __name__ == "__main__":
	print ugly_finder(5)
	