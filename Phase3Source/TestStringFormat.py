import unittest

from StringFormat import StringFormat

class TestStringFormat(unittest.TestCase):

	def test_isPositiveInt(self):

		self.assertTrue(StringFormat.isPositiveInt("324"))
		self.assertTrue(StringFormat.isPositiveInt("6"))
		self.assertTrue(StringFormat.isPositiveInt("1"))
		self.assertTrue(StringFormat.isPositiveInt("0"))

		self.assertFalse(StringFormat.isPositiveInt("-324"))
		self.assertFalse(StringFormat.isPositiveInt("-2"))
		self.assertFalse(StringFormat.isPositiveInt("-1"))

		self.assertFalse(StringFormat.isPositiveInt("3.24"))
		self.assertFalse(StringFormat.isPositiveInt("-0.2"))

		self.assertFalse(StringFormat.isPositiveInt(""))
		self.assertFalse(StringFormat.isPositiveInt(" "))
		self.assertFalse(StringFormat.isPositiveInt("hey"))

if __name__ == '__main__':
    unittest.main()