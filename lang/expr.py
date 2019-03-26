from abc import ABC, abstractmethod
from lang.utils import *

class Expr(ABC,UtilsMixIn):
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

class IntExpr(Expr):
	def __init__(self,value):
		assert isinstance(value,int), "Integer type required"
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

class ArithmeticExpr(BinaryExpr):
	"""
		Abstract base class for arithmetic binary expressions
	"""
	pass

class RelationalExpr(BinaryExpr):
	"""
		Abstract base class for relational binary expressions
	"""
	pass

class LogicalExpr(BinaryExpr):
	"""
		Abstract base class for logical binary expression eg
		and / or
	"""

	#logical Expressions
class AndExpr(LogicalExpr):
	def __str__(self):
		return f"{self.e1} And {self.e2}"


class OrExpr(LogicalExpr):
	def __str__(self):
		return f"{self.e1} Or {self.e2}"


class IdExpr(Expr):
	"""
		IdExpression to reference other expressions
	"""
	def __init__(self,_id):
		self.ref = None
		self.id = _id 

	def __str__(self):
		return f"{self.id}"

class Var:
	"""
		Variable class to hold names
	"""
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return f"{self.name}"

class AbsExpr(Expr):
	"""
		Lambda Expression
	"""
	def __init__(self,var,expr):
		assert isinstance(expr,Expr), "Expression type required, actual: " + type(exp)
		assert isinstance(var,Var), "Variable required"
		self.var = var
		self.expr = expr

	def __str__(self):
		return f"\\{self.var}.{self.expr}"

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
		return f"({self.e1}) ({self.e2})"



	#Arithmetic Expressions

class AddExpr(ArithmeticExpr):
	def __str__(self):
		return f"{self.e1} + {self.e2}"



class SubExpr(ArithmeticExpr):
	def __str__(self):
		return f"{self.e1} - {self.e2}"


class MultExpr(ArithmeticExpr):
	def __str__(self):
		return f"{self.e1} * {self.e2}"


class DivExpr(ArithmeticExpr):
	def __str__(self):
		return f"{self.e1} / {self.e2}"


class RemExpr(ArithmeticExpr):
	def __str__(self):
		return f"{self.e1} % {self.e2}"


#Relational Expressions

class GtExpr(RelationalExpr):
	def __str__(self):
		return f"{self.e1} > {self.e2}"


class LtExpr(RelationalExpr):
	def __str__(self):
		return f"{self.e1} < {self.e2}"


class GteqExpr(RelationalExpr):
	def __str__(self):
		return f"{self.e1} >= {self.e2}"


class LteqExpr(RelationalExpr):
	def __str__(self):
		return f"{self.e1} <= {self.e2}"