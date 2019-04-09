import unittest
from lang.expr import *
from lang import check as c
from lang import *



class BoolTest(unittest.TestCase):
	def setUp(self):
		self.bool_expr = BoolExpr(False)
		self.not_expr = NotExpr(BoolExpr(True))
		self.and_expr = AndExpr(BoolExpr(False),BoolExpr(True))
		self.and_expr_same = AndExpr(BoolExpr(False),BoolExpr(True))
		self.or_expr = OrExpr(BoolExpr(True),NotExpr(BoolExpr(True)))

	def test_height(self):
		self.assertEqual(func.height(self.bool_expr),0)
		self.assertEqual(func.height(self.not_expr),1)
		self.assertEqual(func.height(self.and_expr),1)
		self.assertEqual(func.height(self.or_expr),2)

	def test_value(self):
		self.assertTrue(eval.evaluate(self.or_expr))
		self.assertFalse(eval.evaluate(self.bool_expr))
		self.assertFalse(eval.evaluate(self.and_expr))
		self.assertFalse(eval.evaluate(self.not_expr))

	def test_same(self):
		self.assertFalse(func.same(self.not_expr,self.and_expr))
		self.assertTrue(func.same(self.and_expr,self.and_expr_same))

	def test_size(self):
		self.assertEqual(func.size(self.bool_expr),1)
		self.assertEqual(func.size(self.not_expr),2)
		self.assertEqual(func.size(self.and_expr),3)
		self.assertEqual(func.size(self.or_expr),4)

	def test_string_method(self):
		self.assertEqual(str(self.bool_expr),"False")
		self.assertEqual(str(self.not_expr),"Not True")
		self.assertEqual(str(self.and_expr),"False And True")
		self.assertEqual(str(self.or_expr),"True Or Not True")

	def test_step(self):
		stepped_not = func.step(self.not_expr)
		stepped_and = func.step(self.and_expr)
		stepped_or = func.step(self.or_expr)

		self.assertTrue(isinstance(stepped_not,BoolExpr))
		self.assertTrue(isinstance(stepped_and,BoolExpr))
		self.assertTrue(isinstance(stepped_or,OrExpr))
		self.assertTrue(isinstance(stepped_or.e1,BoolExpr))
		self.assertTrue(isinstance(stepped_or.e2,BoolExpr))

	def test_reduce(self):
		reduced_not = func.reduce(self.not_expr)
		reduced_and = func.reduce(self.and_expr)
		reduced_or = func.reduce(self.or_expr)

		self.assertTrue(isinstance(reduced_not,BoolExpr))
		self.assertTrue(isinstance(reduced_and,BoolExpr))
		self.assertTrue(isinstance(reduced_or,BoolExpr))

	def test_typechecking(self):
		t1 = c.check(self.bool_expr)
		t2 = c.check(self.not_expr)
		t3 = c.check(self.and_expr)
		t4 = c.check(self.and_expr_same)
		t5 = c.check(self.or_expr)

		self.assertEqual(type.boolType,t1)
		self.assertEqual(type.boolType,t2)
		self.assertEqual(type.boolType,t3)
		self.assertEqual(type.boolType,t4)
		self.assertEqual(type.boolType,t5)

		


	
