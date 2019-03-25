from type import *
from expr import *


def is_bool(e):


def is_same_type(t1,t2):

	assert isinstance(t1,Type), "Type expected, actual: " + str(t1)
	assert isinstance(t2,Type), "Type expected, actual: " + str(t2)

	if type(t1) is type(t2):
		return True

	return False

def has_same_type(e1,e2):
	return is_same_type(check(e1),check(e2))

def check_binary(e):

	if e.is_a(ArithmeticExpr):
		if is_same_type(e.e1.type, e.e2.type):
			return intType

		raise Excpetion("Invalid member types for " + str(e))

	if type(e) is (AndExpr,OrExpr):
		return


def do_check(e):

	if type(e) is (BoolExpr,NotExpr):
		return boolType

	if type(e) is BinaryExpr:
		return check_binary(e)


def check(e):
	"""
		Function accepts an expression and returns its type
	"""	

	assert isinstance(e,Expr), "Expression required"

	if not e.type:
		e.type = do_check(e)

	return e.type



