#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	""" test class
	"""
	def test_max(self):
		"""
		test correct output"""
		self.assertAlmostEqual(max_integer([1,2,3,5,7]), 7)
		self.assertAlmostEqual(max_integer([8,2,3,5,1]), 8)
		self.assertAlmostEqual(max_integer([2,5,1]), 5)
		self.assertAlmostEqual(max_integer([-2,-5,-1,-8]), -1)
		self.assertAlmostEqual(max_integer([8,2,-3,5,1]), 8)
		self.assertAlmostEqual(max_integer([-2]), -2)
		self.assertAlmostEqual(max_integer([2]), 2)
		self.assertAlmostEqual(max_integer([]), None)
		self.assertAlmostEqual(max_integer(), None)
		self.assertAlmostEqual(max_integer(["h", "e", "l", "l"]), "l")
		self.assertAlmostEqual(max_integer("hello"), "o")
	def test_raise(self):
		self.assertRaises(TypeError, max_integer, 2)
		

if __name__ == "__main__":
    unittest.main()
