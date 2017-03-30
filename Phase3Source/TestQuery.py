import unittest

from Query import Query
from QueryComponent import QueryComponent
from QueryOperator import QueryOperator

class TestQuery(unittest.TestCase):

	def test_init(self):

		terms = []
		dates = []
		query = Query(terms, dates)
		self.assertEqual(query.terms, terms)
		self.assertEqual(query.dates, dates)

		terms = [QueryComponent("text", "german", QueryOperator.EQUALS),
			QueryComponent("text", "german", QueryOperator.LESS_THAN)]
		dates = []
		query = Query(terms, dates)
		self.assertEqual(query.terms, terms)
		self.assertEqual(query.dates, dates)

		terms = [QueryComponent("text", "german", QueryOperator.EQUALS, False),
			QueryComponent("text", "german", QueryOperator.GREATER_THAN,
				False)]
		dates = []
		query = Query(terms, dates)
		self.assertEqual(query.terms, terms)
		self.assertEqual(query.dates, dates)

		terms = []
		dates = [QueryComponent("date", "2011/01/01", QueryOperator.LESS_THAN),
			QueryComponent("date", "2012/02/01", QueryOperator.GREATER_THAN)]
		query = Query(terms, dates)
		self.assertEqual(query.terms, terms)
		self.assertEqual(query.dates, dates)

		terms = [QueryComponent("text", "german", QueryOperator.EQUALS),
			QueryComponent("text", "german", QueryOperator.GREATER_THAN),
			QueryComponent("text", "german", QueryOperator.EQUALS, False),
			QueryComponent("text", "german", QueryOperator.GREATER_THAN,
				False)]
		dates = [QueryComponent("date", "2011/01/01", QueryOperator.LESS_THAN),
			QueryComponent("date", "2012/02/01", QueryOperator.GREATER_THAN)]
		query = Query(terms, dates)
		self.assertEqual(query.terms, terms)
		self.assertEqual(query.dates, dates)

if __name__ == '__main__':
    unittest.main()