

class Type:
	pass


class BoolType(Type):
	"""
		Represents Boolean type
	"""
	def __str__(self):
		return "bool"


class IntType(Type):
 """
 	Represents integer type
 """
	def __str__(self):
		return "Int"


class ArrowType(Type):
	"""
		Represents Arrow Type:
		T1 -> T2
	"""
	def __init__(self,t1,t2):
		self.t1 = t1
		self.t2 = t2

	def __str__(self):
		return f"{self.t1} -> {self.t2}" 

class FuncType(Type):
	"""
		Represents function type:
		(T1,T2,T3,...Tn) -> Tr
	"""
	def __init__(self,params,ret):
		self.params = params
		self.ret = ret


intType = IntType()

boolType = BoolType()