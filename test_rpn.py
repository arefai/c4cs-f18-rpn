import unittest
import rpn


class TestBasic(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)

	def test_sub(self):
		result = rpn.calculate("4 3 -")
		self.assertEqual(1, result)

	def test_toomany(self):
		with self.assertRaises(ValueError):
			result = rpn.calculate("1 2 3 +")

	def test_carat(self):
		result = rpn.calculate("2 2 ^")
		self.assertEqual(4, result)
