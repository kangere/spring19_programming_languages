from lang.expr import *
from lang import *
import unittest

class CompoundExprTest(unittest.TestCase):

	def setUp(self):
		self.tuple = Tuple(BoolExpr(True),IntExpr(2))
		self.record = Record(x=IntExpr(3),y=BoolExpr(False))

	def test_size(self):
		self.assertEqual(2,self.tuple.size())
		self.assertEqual(2,self.record.size())

	def test_get(self):
		self.assertEqual(True,eval.evaluate(self.tuple.get(0)))
		self.assertEqual(type.boolType,self.tuple.getType(0))
		self.assertEqual(type.intType,self.tuple.getType(1))

		self.assertEqual(False,eval.evaluate(self.record.get('y')))
		self.assertEqual(type.intType,self.record.getType(0))
		self.assertEqual(type.boolType,self.record.getType(1))

	def test_string(self):
		self.assertEqual("{ True: Bool, 2: Int }",str(self.tuple))
		self.assertEqual("{ x=3, y=False }",str(self.record))



	
