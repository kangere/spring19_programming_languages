import unittest
from lang.expr import *
from lang import check as c
from lang import *


class IntTest(unittest.TestCase):

	def setUp(self):
		self.one = IntExpr(1)
		self.two = IntExpr(2)
		self.add = AddExpr(IntExpr(2),IntExpr(1))
		self.sub = SubExpr(IntExpr(2),IntExpr(1))

	def test_typechecking(self):
		t1 = c.check(self.one)
		t2 = c.check(self.two)
		t3 = c.check(self.add)
		t4 = c.check(self.sub)

		self.assertEqual(type.intType,t1)
		self.assertEqual(type.intType,t2)
		self.assertEqual(type.intType,t3)
		self.assertEqual(type.intType,t4)


	def test_evaluation(self):
		self.assertEqual(3,eval.evaluate(self.add))
		self.assertEqual(1,eval.evaluate(self.sub))
