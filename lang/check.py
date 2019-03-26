from type import *
from expr import *


def is_bool(e):
	return check(e) == boolType

def is_int(e):
	return check(e) == intType

def is_same_type(t1,t2):

	assert isinstance(t1,Type), "Type expected, actual: " + str(t1)
	assert isinstance(t2,Type), "Type expected, actual: " + str(t2)

	if type(t1) is type(t2):
		return True

	return False

def has_same_type(e1,e2):
	return is_same_type(check(e1),check(e2))

def check_binary(e):

	if e.is_a(RelationalExpr):
		if  has_same_type(e.e1, e.e2):
			return boolType	

		raise Excpetion("Member types must be the same" + str(e))
		

	if e.is_a(LogicalExpr):
		if is_bool(e.e1) and is_bool(e.e2): 
			return boolType

		raise Excpetion("Boolean Type expected, actual: " + str(e.e1) + str(e.e2))

	if e.is_a(ArithmeticExpr):
		if is_int(e.e1) and is_int(e.e2):
			return intType

		raise Excpetion("Integer Type expected, actual: " + str(e.e1) + str(e.e2))

def do_check(e):

	if e.is_a(BoolExpr):
		return boolType

	if e.is_a(IntExpr):
		return intType 

	if e.is_a(BinaryExpr):
		return check_binary(e)


def check(e):
	"""
		Function accepts an expression and returns its type
	"""	

	assert isinstance(e,Expr), "Expression required"

	if not e.type:
		e.type = do_check(e)

	return e.type



