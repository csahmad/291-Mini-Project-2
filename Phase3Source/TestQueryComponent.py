import unittest

from QueryComponent import QueryComponent
from QueryOperator import QueryOperator

class TestQueryComponent(unittest.TestCase):

	def test_value(self):

		component = QueryComponent("german", QueryOperator.EQUALS)
		self.assertEqual(component.value, "german")

		component = QueryComponent("2011/01/01", QueryOperator.EQUALS)
		self.assertEqual(component.value, "2011/01/01")

	def test_operator(self):

		component = QueryComponent("german", QueryOperator.EQUALS)
		self.assertEqual(component.operator, QueryOperator.EQUALS)

		component = QueryComponent("german", QueryOperator.LESS_THAN)
		self.assertEqual(component.operator, QueryOperator.LESS_THAN)

		component = QueryComponent("german", QueryOperator.GREATER_THAN)
		self.assertEqual(component.operator, QueryOperator.GREATER_THAN)

if __name__ == '__main__':
    unittest.main()