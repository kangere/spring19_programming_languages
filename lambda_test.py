import unittest
from lang.expr import *
from lang.func import *
from lang.check import *
from lang.type import *



class LambdaTest(unittest.TestCase):

	def setUp(self):
		self.true_lambda = AbsExpr(Var("a"),AbsExpr(Var("b"),IdExpr("a")))
		self.false_lambda = AbsExpr(Var("a"),AbsExpr(Var("b"),IdExpr("b")))
		self.land = \
					  AbsExpr(Var("p"), 
					    AbsExpr(Var("q"), 
					      AppExpr(
					        AppExpr(
					          IdExpr("p"), 
					          IdExpr("q")),
					        IdExpr("p"))))

		self.typed_lambda = AbsExpr(VarDecl("p",intType),AddExpr(IntExpr(1),IdExpr("p")))



	def test_string_method(self):
		self.assertEqual(str(self.true_lambda),"\\a.\\b.a")
		self.assertEqual(str(self.false_lambda),"\\a.\\b.b")
		self.assertEqual(str(self.land),"\\p.\\q.p q p")

	#TODO:fix
	def test_untyped_application(self):
		e1 = AppExpr(AppExpr(self.land,self.true_lambda),self.false_lambda)
		resolve(e1)

		e = e1	
		while is_reducible(e):
			e = step(e)
			print(e)

		print(e)

	def test_typed_lambda(self):
		resolve(self.typed_lambda)

		t = check(self.typed_lambda)

		self.assertTrue(isinstance(t,ArrowType))
		self.assertEqual(t.param,intType)
		self.assertEqual(t.ret,intType)



	
		





		