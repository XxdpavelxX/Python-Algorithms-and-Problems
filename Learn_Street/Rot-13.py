from string import ascii_uppercase, ascii_lowercase
import math

def string_rot13(str):
    # ROT-13 is a simple substitution cypher. It stands for
    # "ROTate by 13 places." The cypher replaces any letter
    # (a-z or A-Z) with the one that appears 13 sequential places
    # behind it. Note that for the last half of the alphabet, the
    # ROT-13 character loops back around to the beginning of the
    # alphabet. Also note that characters that aren't in the alphabet
    # are passed through.
	"Return a string in its ROT-13 format"
	total = []
	"REPLACE THIS CODE WITH ROT-13 METHOD"
	
	for char in str:
		a = ord(char)+13   #new numerical value that shall later be converted to number
		if ord(char)>109:
			a = 97 + (a - 123) #109+13+1=123 which is first ord value for lowerercase letter that goes above alphabet
			total.append(chr(a))
		elif 77<ord(char)<84:
			a = 65 + (a - 91)   #77+13+1= 91 which is first ord value for uppercase letters that goes above alphabet
			total.append(chr(a))
		elif 65>ord(char) or 90<ord(char)<97 or ord(char)>122:  #for chars that are not alphabetic
			pass   
		else:
			total.append(chr(a))   #all regular letters that do not go below or above alphabet value
	coded = ''.join(total)
	print (coded)

if __name__ == "__main__":
	string_rot13(input("Input the text to be coded here, include quotation marks at beginning and end: "))