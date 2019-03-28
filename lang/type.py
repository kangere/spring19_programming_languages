

class Type:
	"""
		Base class for all types
	"""
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
	def __init__(self,param,ret):
		self.param = param
		self.ret = ret

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

	def __str__(self):
		return f"{' '.join(map(str,self.params))} -> {self.ret}"


intType = IntType()

boolType = BoolType()