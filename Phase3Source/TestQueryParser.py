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

		terms = []
		dates = []
		componentString = "text:hey"
		QueryParser._addComponent(componentString, terms, dates)
		self.assertEqual(terms,
			[QueryComponent("hey", QueryOperator.EQUALS)])
		self.assertEqual(dates, [])

		terms = []
		dates = []
		componentString = "text:hey%"
		QueryParser._addComponent(componentString, terms, dates)
		self.assertEqual(terms,
			[QueryComponent("hey", QueryOperator.EQUALS, False)])
		self.assertEqual(dates, [])

		terms = []
		dates = []
		componentString = "date:2011/01/21"
		QueryParser._addComponent(componentString, terms, dates)
		self.assertEqual(terms, [])
		self.assertEqual(dates,
			[QueryComponent("2011/01/21", QueryOperator.EQUALS)])

		terms = []
		dates = []
		componentString = "date>2011/01/21"
		QueryParser._addComponent(componentString, terms, dates)
		self.assertEqual(terms, [])
		self.assertEqual(dates,
			[QueryComponent("2011/01/21", QueryOperator.GREATER_THAN)])

		terms = []
		dates = []
		componentString = "date<2011/01/21"
		QueryParser._addComponent(componentString, terms, dates)
		self.assertEqual(terms, [])
		self.assertEqual(dates,
			[QueryComponent("2011/01/21", QueryOperator.LESS_THAN)])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("text=hey", [], [])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("date=2011/01/21", [], [])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("date2011/01/21", [], [])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("date", [], [])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("2011/01/21", [], [])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("text", [], [])

		with self.assertRaises(ValueError):
			QueryParser._addComponent("hey", [], [])

	def test_eq(self):

		a = Query(
			[],
			[])
		b = Query(
			[],
			[])
		self.assertEqual(a, b)

		a = Query(
			[],
			[QueryComponent("2011/02/21", QueryOperator.EQUALS)])
		b = Query(
			[],
			[QueryComponent("2011/02/21", QueryOperator.EQUALS)])
		self.assertEqual(a, b)

		a = Query(
			[QueryComponent("hey", QueryOperator.EQUALS),
				QueryComponent("a", QueryOperator.LESS_THAN, False)],
			[QueryComponent("2011/02/21", QueryOperator.EQUALS)])
		b = Query(
			[QueryComponent("hey", QueryOperator.EQUALS),
				QueryComponent("a", QueryOperator.LESS_THAN, False)],
			[QueryComponent("2011/02/21", QueryOperator.EQUALS)])
		self.assertEqual(a, b)

		a = Query(
			[QueryComponent("hey", QueryOperator.EQUALS),
				QueryComponent("a", QueryOperator.LESS_THAN, False)],
			[QueryComponent("2011/02/21", QueryOperator.LESS_THAN)])
		b = Query(
			[QueryComponent("hey", QueryOperator.EQUALS),
				QueryComponent("a", QueryOperator.LESS_THAN, False)],
			[QueryComponent("2011/02/21", QueryOperator.EQUALS)])
		self.assertNotEqual(a, b)

		a = Query(
			[QueryComponent("hey", QueryOperator.EQUALS),
				QueryComponent("abc", QueryOperator.LESS_THAN, False)],
			[QueryComponent("2011/02/21", QueryOperator.EQUALS)])
		b = Query(
			[QueryComponent("hey", QueryOperator.EQUALS),
				QueryComponent("a", QueryOperator.LESS_THAN, False)],
			[QueryComponent("2011/02/21", QueryOperator.EQUALS)])
		self.assertNotEqual(a, b)

	def test_parse(self):

		string = "text:hey"
		result = QueryParser.parse(string)
		expected = Query(
			[QueryComponent("hey", QueryOperator.EQUALS)],
			[])
		self.assertEqual(result, expected)

		string = "text:hey%"
		result = QueryParser.parse(string)
		expected = Query(
			[QueryComponent("hey", QueryOperator.EQUALS, False)],
			[])
		self.assertEqual(result, expected)

		string = "date:2011/02/21"
		result = QueryParser.parse(string)
		expected = Query(
			[],
			[QueryComponent("2011/02/21", QueryOperator.EQUALS)])
		self.assertEqual(result, expected)

		string = "date<2011/02/21"
		result = QueryParser.parse(string)
		expected = Query(
			[],
			[QueryComponent("2011/02/21", QueryOperator.LESS_THAN)])
		self.assertEqual(result, expected)

		string = "date>2011/02/21"
		result = QueryParser.parse(string)
		expected = Query(
			[],
			[QueryComponent("2011/02/21", QueryOperator.GREATER_THAN)])

		string = "text:hey date>2011/02/21"
		result = QueryParser.parse(string)
		expected = Query(
			[QueryComponent("hey", QueryOperator.EQUALS)],
			[QueryComponent("2011/02/21", QueryOperator.GREATER_THAN)])

		string = "text:hey% date>2011/02/21"
		result = QueryParser.parse(string)
		expected = Query(
			[QueryComponent("hey", QueryOperator.EQUALS, False)],
			[QueryComponent("2011/02/21", QueryOperator.GREATER_THAN)])

		with self.assertRaises(ValueError):
			QueryParser.parse("")

		with self.assertRaises(ValueError):
			QueryParser.parse(" ")

if __name__ == '__main__':
    unittest.main()