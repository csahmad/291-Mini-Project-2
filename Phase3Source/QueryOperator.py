from enum import Enum

class QueryOperator(Enum):
	"""An operator used in a query"""

	EQUALS = 0
	LESS_THAN = 1
	GREATER_THAN = 2