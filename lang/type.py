

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
		return "Bool"


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

class TupleType(Type):
	"""
		Represents the tuple type:
		{T1,T2,.....Tn}
	"""
	def __init__(self):
		self.types = []
		self.numTypes = 0

	def add(self,t):
		assert isinstance(t,Type), "Type required"
		self.types.append(t)
		self.numTypes += 1

	def get(self,index):
		if index >= self.numTypes and index < 0:
			raise Exception("Index out of bounds")
		return self.types[index]

	def size(self):
		return self.numTypes

	def __str__(self):
		return f"{' '.join(map(str,self.types))}" 


class IdType(Type):

	def __init__(self,name):
		self.name = name


class AbsType(Type):
	
	def __init__(self,var,expr):
		self.var = var
		self.expr = expr

class AppType(Type):
	
	def __init__(self,t1,t2):
		assert isinstance(t1,Type)
		assert isinstance(t2,Type)
		self.t1 = t1
		self.t2 = t2

intType = IntType()

boolType = BoolType()