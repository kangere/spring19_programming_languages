import unittest
from lang.expr import *
from lang.func import *



class LambdaTest(unittest.TestCase):

	def setUp(self):
		self.true_lambda = AbsExpr(Var("a"),AbsExpr(Var("b"),IdExpr("a")))
		self.false_lambda = AbsExpr(Var("a"),AbsExpr(Var("b"),IdExpr("b")))
		self.land = \
					  AbsExpr("p", 
					    AbsExpr("q", 
					      AppExpr(
					        AppExpr(
					          IdExpr("p"), 
					          IdExpr("q")),
					        IdExpr("p"))))



	def test_string_method(self):
		self.assertEqual(str(self.true_lambda),"\\a.\\b.a")
		self.assertEqual(str(self.false_lambda),"\\a.\\b.b")
		self.assertEqual(str(self.land),"\\p.\\q.p q p")

	
		





		