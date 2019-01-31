

class Expr:
	"""	Base class for all expressions """
	pass

class BoolExpr(Expr):
	def __init__(self,value):
		assert isinstance(value,bool), "Boolean type required"
		self.value = value

	def __str__(self):
		return str(self.value)

class NotExpr(Expr):
	def __init__(self,e1):
		assert isinstance(e1,Expr), "Expression Type required"
		self.e1 = e1;

	def __str__(self):
		return "Not " + str(self.e1)

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
		return str(self.e1) + " And " + str(self.e2)


class OrExpr(BinaryExpr):
	def __str__(self):
		return str(self.e1) + " Or " + str(self.e2)