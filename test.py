import unittest
import func
from expr import *

class ExprTest(unittest.TestCase):
	def test_height(self):
		bool_expr = BoolExpr(False)
		not_expr = NotExpr(BoolExpr(True))
		and_expr = AndExpr(BoolExpr(False),BoolExpr(True))
		or_expr = OrExpr(BoolExpr(True),NotExpr(BoolExpr(True)))

		self.assertEqual(func.height(bool_expr),0)
		self.assertEqual(func.height(not_expr),1)
		self.assertEqual(func.height(and_expr),1)
		self.assertEqual(func.height(or_expr),2)

	def test_value(self):
		bool_expr = BoolExpr(False)
		not_expr = NotExpr(BoolExpr(True))
		and_expr = AndExpr(BoolExpr(False),BoolExpr(True))
		or_expr = OrExpr(BoolExpr(True),NotExpr(BoolExpr(True)))

		self.assertTrue(func.value(or_expr))
		self.assertFalse(func.value(bool_expr))
		self.assertFalse(func.value(and_expr))
		self.assertFalse(func.value(not_expr))

	def test_same(self):
		not_expr = NotExpr(BoolExpr(True))
		and_expr = AndExpr(BoolExpr(False),BoolExpr(True))

		self.assertTrue(func.same(not_expr,and_expr))


if __name__ == '__main__':
	unittest.main()
