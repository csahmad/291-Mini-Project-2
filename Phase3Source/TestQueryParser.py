import unittest

from QueryParser import QueryParser
from Query import Query
from QueryComponent import QueryComponent
from QueryOperator import QueryOperator

class TestQueryParser(unittest.TestCase):

	def test_getDateFormat(self):

		self.assertEqual(QueryParser._getDateFormat(), "yyyy/MM/dd")

	def test_validateDate(self):

		QueryParser._validateDate("2005/09/24")
		QueryParser._validateDate("1998/11/02")

		with self.assertRaises(ValueError):
			QueryParser._validateDate("2005/09/32")

		with self.assertRaises(ValueError):
			QueryParser._validateDate("2005/13/24")

		with self.assertRaises(ValueError):
			QueryParser._validateDate("2005/00/24")

		with self.assertRaises(ValueError):
			QueryParser._validateDate("2005/09/00")

		with self.assertRaises(ValueError):
			QueryParser._validateDate("2005/9/24")

		with self.assertRaises(ValueError):
			QueryParser._validateDate("2005/09/4")

		with self.assertRaises(ValueError):
			QueryParser._validateDate("205/09/24")

		with self.assertRaises(ValueError):
			QueryParser._validateDate("20005/09/24")

		with self.assertRaises(ValueError):
			QueryParser._validateDate("2005-09-24")

		with self.assertRaises(ValueError):
			QueryParser._validateDate("2005/09/24/02")

		with self.assertRaises(ValueError):
			QueryParser._validateDate("2005/09")

	def test_hasWildcard(self):

		self.assertTrue(QueryParser._hasWildcard("a%"))
		self.assertTrue(QueryParser._hasWildcard("hey%"))

		self.assertFalse(QueryParser._hasWildcard("a"))
		self.assertFalse(QueryParser._hasWildcard("hey"))

		with self.assertRaises(ValueError):
			QueryParser._hasWildcard("%a")

		with self.assertRaises(ValueError):
			QueryParser._hasWildcard("%hey")

		with self.assertRaises(ValueError):
			QueryParser._hasWildcard("he%y")

		with self.assertRaises(ValueError):
			QueryParser._hasWildcard("hey%%")

	def test_removeWildcard(self):

		self.assertEqual(QueryParser._removeWildcard("a%"), "a")
		self.assertEqual(QueryParser._removeWildcard("hey%"), "hey")

	def test_addComponent(self):

		exactTerms = []
		startsWith = []
		dates = []
		componentString = "text:hey"
		QueryParser._addComponent(componentString, exactTerms, startsWith,
			dates)
		self.assertEqual(exactTerms,
			[QueryComponent("hey", QueryOperator.EQUALS)])
		self.assertEqual(startsWith, [])
		self.assertEqual(dates, [])

		exactTerms = []
		startsWith = []
		dates = []
		componentString = "text:hey%"
		QueryParser._addComponent(componentString, exactTerms, startsWith,
			dates)
		self.assertEqual(exactTerms, [])
		self.assertEqual(startsWith,
			[QueryComponent("hey", QueryOperator.EQUALS)])
		self.assertEqual(dates, [])

		exactTerms = []
		startsWith = []
		dates = []
		componentString = "date:2011/01/21"
		QueryParser._addComponent(componentString, exactTerms, startsWith,
			dates)
		self.assertEqual(exactTerms, [])
		self.assertEqual(startsWith, [])
		self.assertEqual(dates,
			[QueryComponent("2011/01/21", QueryOperator.EQUALS)])

		exactTerms = []
		startsWith = []
		dates = []
		componentString = "date>2011/01/21"
		QueryParser._addComponent(componentString, exactTerms, startsWith,
			dates)
		self.assertEqual(exactTerms, [])
		self.assertEqual(startsWith, [])
		self.assertEqual(dates,
			[QueryComponent("2011/01/21", QueryOperator.GREATER_THAN)])

		exactTerms = []
		startsWith = []
		dates = []
		componentString = "date<2011/01/21"
		QueryParser._addComponent(componentString, exactTerms, startsWith,
			dates)
		self.assertEqual(exactTerms, [])
		self.assertEqual(startsWith, [])
		self.assertEqual(dates,
			[QueryComponent("2011/01/21", QueryOperator.LESS_THAN)])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("text=hey", [], [], [])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("date=2011/01/21", [], [], [])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("date2011/01/21", [], [], [])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("date", [], [], [])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("2011/01/21", [], [], [])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("text", [], [], [])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("hey", [], [], [])

	def test_parse(self):

		pass

if __name__ == '__main__':
    unittest.main()