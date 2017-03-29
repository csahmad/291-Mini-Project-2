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

		terms = [QueryComponent("german", QueryOperator.EQUALS),
			QueryComponent("german", QueryOperator.LESS_THAN)]
		dates = []
		query = Query(terms, dates)
		self.assertEqual(query.terms, terms)
		self.assertEqual(query.dates, dates)

		terms = [QueryComponent("german", QueryOperator.EQUALS, False),
			QueryComponent("german", QueryOperator.GREATER_THAN, False)]
		dates = []
		query = Query(terms, dates)
		self.assertEqual(query.terms, terms)
		self.assertEqual(query.dates, dates)

		terms = []
		dates = [QueryComponent("2011/01/01", QueryOperator.LESS_THAN),
			QueryComponent("2012/02/01", QueryOperator.GREATER_THAN)]
		query = Query(terms, dates)
		self.assertEqual(query.terms, terms)
		self.assertEqual(query.dates, dates)

		terms = [QueryComponent("german", QueryOperator.EQUALS),
			QueryComponent("german", QueryOperator.GREATER_THAN),
			QueryComponent("german", QueryOperator.EQUALS, False),
			QueryComponent("german", QueryOperator.GREATER_THAN, False)]
		dates = [QueryComponent("2011/01/01", QueryOperator.LESS_THAN),
			QueryComponent("2012/02/01", QueryOperator.GREATER_THAN)]
		query = Query(terms, dates)
		self.assertEqual(query.terms, terms)
		self.assertEqual(query.dates, dates)

if __name__ == '__main__':
    unittest.main()