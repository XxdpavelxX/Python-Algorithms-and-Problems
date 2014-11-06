__author__ = 'xxdpavelxx'
import unittest
list_of_vals=[('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]

def IntegerToRoman(given_inp):   #This only works correctly for numbers under 5,000. given_inp should be in int type.
    roman_nums = []
    for roman, number in list_of_vals:
        while number <= given_inp:
            given_inp -=number
            roman_nums.append(roman)
    return ''.join(roman_nums)


def RomanToInteger(given_inp):  # make sure string is in str type.
    ans = 0
    roman_nums=[]
    for roman,number in list_of_vals:
        roman_nums.append(roman)
    for x in given_inp:
        if x not in roman_nums:
            raise Exception("BadRomanNumeral")

    for roman, number in list_of_vals:
        while given_inp.startswith(roman):
            ans = ans+number
            given_inp = given_inp[len(roman):]
    return ans



class Testtitle(unittest.TestCase):   #Normally write tests on separate file.
    def test_IntegerToRoman(self):
        self.assertEqual(IntegerToRoman(11), 'XI')
        self.assertEqual(IntegerToRoman(369), 'CCCLXIX')
        self.assertEqual(IntegerToRoman(4999),'MMMMCMXCIX')

    def test_RomanToInteger(self):
        self.assertEqual(RomanToInteger('XV'),15)
        self.assertEqual(RomanToInteger('CVI'), 106)
        self.assertEqual(RomanToInteger('MMCLXI'),2161)

if __name__ == '__main__':
    unittest.main()



#alternante
#def RomanToInteger(string):
    #list_of_vals2=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
  #  answer=0
   # for conversions in list_of_vals2:
    #    continueyes=True
     #   while continueyes:
      #      if len(string)>=len(conversions[0]):
       #         if string[0:len(conversions[0])]==conversions[0]:
        #            answer=answer+ conversions[1]
         #           string=string[len(conversions[0]):]

#                else: continueyes=False
 #           else: continueyes=False
  #  return answer