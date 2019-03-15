
#Adds utility functions to inheriting classes
class UtilsMixIn:
	"""
		Adds easier type checking for Child Classes
	"""
	def is_a(self,someType):
		return isinstance(self,someType)

	"""
		Returns string listing all attributes and values of a particular
		instance
	"""
	def attrnames(self):
		result = ''
		for attr in sorted(self.__dict__):
			result += '\t%s = %s \n' % (attr,self.__dict__[attr])
		return result

