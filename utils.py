
class TypeCheckerMixIn:
	"""
		Adds easier type checking for Expressions
	"""
	def is_a(self,someType):
		return isinstance(self,someType)