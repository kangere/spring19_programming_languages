from lang.expr import *
from lang import *
import unittest

class CompoundExprTest(unittest.TestCase):

	def setUp(self):
		self.tuple = Tuple(BoolExpr(True),IntExpr(2))

	def test_size(self):
		self.assertEqual(2,self.tuple.size())

	def test_get(self):
		self.assertEqual(True,eval.evaluate(self.tuple.get(0)))
		self.assertEqual(type.boolType,self.tuple.getType(0))
		self.assertEqual(type.intType,self.tuple.getType(1))

	def test_string(self):
		self.assertEqual("{ True: Bool, 2: Int }",str(self.tuple))



	
