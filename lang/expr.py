from abc import ABC, abstractmethod
from lang.utils import *
from lang.type import *


class Expr(ABC,UtilsMixIn):
	"""	Abstract Base class for all expressions """
	def __init__(self):
		self.type = None

	@abstractmethod
	def __str__(self):
		pass

class BoolExpr(Expr):
	def __init__(self,value):
		assert isinstance(value,bool), "Boolean type required"
		Expr.__init__(self)
		self.value = value

	def __str__(self):
		return f"{self.value}"

class IntExpr(Expr):
	def __init__(self,value):
		assert isinstance(value,int), "Integer type required"
		Expr.__init__(self)
		self.value = value

	def __str__(self):
		return f"{self.value}"

		
class NotExpr(Expr):
	def __init__(self,e1):
		assert isinstance(e1,Expr), "Expression Type required"
		Expr.__init__(self)
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
		Expr.__init__(self)
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
	pass

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
		Expr.__init__(self)
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

class VarDecl:
	"""
		Variable class that also holds type information
	"""
	def __init__(self,name,t):
		self.name = name
		self.t = t 

	def __str__(self):
		return f"{self.name} : {self.t}"


class AbsExpr(Expr):
	"""
		Lambda Expression
	"""
	def __init__(self,var,expr):
		assert isinstance(expr,Expr), "Expression type required, actual: " + type(exp)
		assert type(var) in (Var,VarDecl), "Variable required"
		Expr.__init__(self)
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
		Expr.__init__(self)
		self.e1 = e1
		self.e2 = e2

	def __str__(self):
		return f"{self.e1} {self.e2}"



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


class EqExpr(RelationalExpr):
	def __str__(self):
		return f"{self.e1} == {self.e2}"

class NtEqExpr(RelationalExpr):
	def __str__(self):
		return f"{self.e1} != {self.e2}"




#Compund Expressions 

import lang.check as c

class Tuple(Expr):
	"""
		Tuple implementation
	"""
	def __init__(self,*args):
		Expr.__init__(self)
		self.listItems = []
		self.type = TupleType()
		for arg in args:
			if isinstance(arg,Expr):
				self.listItems.append(arg)
				self.type.add(c.check(arg))
			else:
				raise TypeError("Expression required, found")
		self.numMembers = len(self.listItems)


	def size(self):
		return self.numMembers

	def get(self,index):
		if index >= self.numMembers and index < 0:
			raise Exception("Index is out of bounds")
		return self.listItems[index]

	def getType(self,index):
		if index >= self.numMembers and index < 0:
			raise Exception("Index is out of bounds")
		return self.type.get(index)

	def __str__(self):
		s = '{ '
		for i,expr in enumerate(self.listItems):
			s += str(expr) + ": " + str(self.type.get(i))
			s += ", "
		
		s = s[:len(s)-2] + ' }'
		return s


