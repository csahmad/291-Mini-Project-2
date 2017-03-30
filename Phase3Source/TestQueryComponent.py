import unittest

from QueryComponent import QueryComponent
from QueryOperator import QueryOperator

class TestQueryComponent(unittest.TestCase):

	def test_value(self):

		component = QueryComponent("text", "german", QueryOperator.EQUALS)
		self.assertEqual(component.value, "german")

		component = QueryComponent("date", "2011/01/01", QueryOperator.EQUALS)
		self.assertEqual(component.value, "2011/01/01")

	def test_operator(self):

		component = QueryComponent("text", "german", QueryOperator.EQUALS)
		self.assertEqual(component.operator, QueryOperator.EQUALS)

		component = QueryComponent("text", "german", QueryOperator.LESS_THAN)
		self.assertEqual(component.operator, QueryOperator.LESS_THAN)

		component = QueryComponent("text", "german",
			QueryOperator.GREATER_THAN)
		self.assertEqual(component.operator, QueryOperator.GREATER_THAN)

	def test_eq(self):

		a = QueryComponent("text", "german", QueryOperator.EQUALS)
		b = QueryComponent("text", "german", QueryOperator.EQUALS)
		self.assertEqual(a, b)

		a = QueryComponent("name", "german", QueryOperator.EQUALS)
		b = QueryComponent("text", "german", QueryOperator.EQUALS)
		self.assertNotEqual(a, b)

		a = QueryComponent("text", "german", QueryOperator.EQUALS)
		b = QueryComponent("text", "german", QueryOperator.EQUALS, False)
		self.assertNotEqual(a, b)

		a = QueryComponent("text", "germa", QueryOperator.EQUALS)
		b = QueryComponent("text", "german", QueryOperator.EQUALS)
		self.assertNotEqual(a, b)

		a = QueryComponent("text", "german", QueryOperator.EQUALS)
		b = QueryComponent("text", "german", QueryOperator.LESS_THAN)
		self.assertNotEqual(a, b)

if __name__ == '__main__':
    unittest.main()