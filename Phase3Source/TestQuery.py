import unittest

from Query import Query
from QueryComponent import QueryComponent
from QueryOperator import QueryOperator

class TestQuery(unittest.TestCase):

	def test_init(self):

		exactTerms = []
		startsWith = []
		dates = []
		query = Query(exactTerms, startsWith, dates)
		self.assertEqual(query.exactTerms, exactTerms)
		self.assertEqual(query.startsWith, startsWith)
		self.assertEqual(query.dates, dates)

		exactTerms = [QueryComponent("german", QueryOperator.EQUALS),
			QueryComponent("german", QueryOperator.LESS_THAN)]
		startsWith = []
		dates = []
		query = Query(exactTerms, startsWith, dates)
		self.assertEqual(query.exactTerms, exactTerms)
		self.assertEqual(query.startsWith, startsWith)
		self.assertEqual(query.dates, dates)

		exactTerms = []
		startsWith = [QueryComponent("german", QueryOperator.EQUALS),
			QueryComponent("german", QueryOperator.GREATER_THAN)]
		dates = []
		query = Query(exactTerms, startsWith, dates)
		self.assertEqual(query.exactTerms, exactTerms)
		self.assertEqual(query.startsWith, startsWith)
		self.assertEqual(query.dates, dates)

		exactTerms = []
		startsWith = []
		dates = [QueryComponent("2011/01/01", QueryOperator.LESS_THAN),
			QueryComponent("2012/02/01", QueryOperator.GREATER_THAN)]
		query = Query(exactTerms, startsWith, dates)
		self.assertEqual(query.exactTerms, exactTerms)
		self.assertEqual(query.startsWith, startsWith)
		self.assertEqual(query.dates, dates)

		exactTerms = [QueryComponent("german", QueryOperator.EQUALS),
			QueryComponent("german", QueryOperator.GREATER_THAN)]
		startsWith = [QueryComponent("german", QueryOperator.EQUALS),
			QueryComponent("german", QueryOperator.GREATER_THAN)]
		dates = [QueryComponent("2011/01/01", QueryOperator.LESS_THAN),
			QueryComponent("2012/02/01", QueryOperator.GREATER_THAN)]
		query = Query(exactTerms, startsWith, dates)
		self.assertEqual(query.exactTerms, exactTerms)
		self.assertEqual(query.startsWith, startsWith)
		self.assertEqual(query.dates, dates)

if __name__ == '__main__':
    unittest.main()