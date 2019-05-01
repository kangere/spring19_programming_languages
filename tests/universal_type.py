import unittest
from lang.type import *
from lang.expr import * 
from lang.func import *


class UniversalTypeTest(unittest.TestCase):

	def setUp(self):
		self.uType = IdType('X')

		#lambda expression with Universaly Quantified type
		self.expr = AbsExpr(VarDecl('x',self.uType),IdExpr('x'))
		#Type Abstraction : \X. \x:X. x
		self.absType = AbsType('X',self.expr)

		#Type Application
		#(\T.\x:T.x  [int])
		self.appType = AppType(self.absType,intType)

	def test_typeApplication(self):

		#expression generated after type application
		#in this case integer type
		newExpr = app_type(self.appType)

		self.assertEqual(newExpr.var.t, intType)
