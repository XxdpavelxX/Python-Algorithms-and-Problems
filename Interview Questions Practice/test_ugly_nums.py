import unittest
import ugly_nums

class Testtitle(unittest.TestCase):
	def test_ugly_nums(self):
		self.assertEqual(ugly_nums.ugly_finder(2),60)
		self.assertEqual(ugly_nums.ugly_finder(11),330)
		
if __name__ == "__main__":
	unittest.main()
		