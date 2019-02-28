from abc import ABC, abstractmethod
from utils import *

class Expr(TypeCheckerMixIn,ABC):
	"""	Abstract Base class for all expressions """
	@abstractmethod
	def __str__(self):
		pass

class BoolExpr(Expr):
	def __init__(self,value):
		assert isinstance(value,bool), "Boolean type required"
		self.value = value

	def __str__(self):
		return f"{self.value}"

class NotExpr(Expr):
	def __init__(self,e1):
		assert isinstance(e1,Expr), "Expression Type required"
		self.e1 = e1;

	def __str__(self):
		return f"Not {self.e1}"

class BinaryExpr(Expr):
	"""
		Base class for expression classes with two member expressions
	"""
	def __init__(self,e1,e2):
		assert isinstance(e1,Expr), "Expression Type required"
		assert isinstance(e2,Expr), "Expression Type required"
		self.e1 = e1
		self.e2 = e2


class AndExpr(BinaryExpr):
	def __str__(self):
		return f"{self.e1} And {self.e2}"


class OrExpr(BinaryExpr):
	def __str__(self):
		return f"{self.e1} Or {self.e2}"


class IdExpr(Expr):
	"""
		IdExpression to reference other expressions
	"""
	def __init__(self,_id):
		self.ref = None
		self._id = _id 

	def __str__(self):
		return f"{self._id} -> {self.ref}"

class Var:
	"""
		Variable class to hold names
	"""
	def __init__(self,name):
		self._name = name

class AbsExpr(Expr):
	"""
		Lambda Expression
	"""
	def __init__(self,var,expr):
		assert isinstance(exp,IdExpr), "Expression type required, actual: " + type(exp)
		self.var = var
		self.expr = expr

	def __str__(self):
		return f"\\{self.var._name}.{self.expr}"

class AppExpr(Expr):
	"""
		Application Expression 
	"""
	def __init__(self,e1,e2):
		assert isinstance(e1,Expr), "Expression type required, actual: " +type(e1)
		assert isinstance(e2,Expr), "Expression type required, actual: " +type(e2)
		self.e1 = e1
		self.e2 = e2

	def __str__(self):
		return f"{self.e1} {self.e2}"


