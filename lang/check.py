from lang.type import *
from lang.expr import *


def is_bool(e):
	return check(e) == boolType

def is_int(e):
	return check(e) == intType

def is_same_type(t1,t2):

	assert isinstance(t1,Type), "Type expected, found: " + str(t1)
	assert isinstance(t2,Type), "Type expected, found: " + str(t2)

	if type(t1) is type(t2):
		return True

	return False

def has_same_type(e1,e2):
	return is_same_type(check(e1),check(e2))

def check_not(e):
	if is_bool(e.e1):
		return boolType

	raise TypeError("Boolean type expected, found: " + str(e.e1))



def check_binary(e):

	if e.is_a(RelationalExpr):
		# G |- e1 : T1   G |- e2 : T2
		# --------------------------- T-Eq
		#    G |- e1 op e2 : Bool
		if  has_same_type(e.e1, e.e2):
			return boolType	

		raise Exception("Member types must be the same" + str(e))
		

	if e.is_a(LogicalExpr):
		# G |- e1 : Bool   G |- e2 : Bool
		# ------------------------------- T-And
		#    G |- e1 op e2 : Bool
		if is_bool(e.e1) and is_bool(e.e2): 
			return boolType

		raise Exception("Boolean Type expected, found: " + str(e.e1) + str(e.e2))

	if e.is_a(ArithmeticExpr):
		# G |- e1 : Int   G |- e2 : Int
		# ----------------------------- T-Add
		#      G |- e1 op e2 : Int

		if is_int(e.e1) and is_int(e.e2):
			return intType

		raise Exception("Integer Type expected, found: " + str(e.e1) + str(e.e2))


def check_abs(e):
	#   G, x:T1 |- e1 : T2
	# ------------------------ T-abs
	# G |- \x:T1.e1 : T1 -> T2

	t1 = e.var.t
	t2 = check(e.expr)
	return ArrowType(t1,t2)

def check_app(e):
	# G |- e1 : T1 -> T2   G |- e2 : T1
 	# ---------------------------------
  	#        G |- e1 e2 : T2

	t1 = check(e.e1)

	if type(t1) is not ArrowType:
		raise TypeError("Arrow type expected, found: " + str(t1))

	t2 = check(e.e2)

	if not is_same_type(t1.param,t2):
		raise TypeError(str(t1.param) + " type expected, found: " + str(t2))
	return t1.ret

def do_check(e):

	if e.is_a(BoolExpr):
		return boolType

	if e.is_a(IntExpr):
		return intType 

	if e.is_a(IdExpr):
		if e.ref.t is None:
			raise TypeError("Id does not have a type")
		return e.ref.t

	if e.is_a(NotExpr):
		return check_not(e)

	if e.is_a(BinaryExpr):
		return check_binary(e)

	if e.is_a(AbsExpr):
		return check_abs(e)

	if e.is_a(AppExpr):
		return check_app(e)


def check(e):
	"""
		Function accepts an expression and returns its type
	"""	

	assert isinstance(e,Expr), "Expression required"

	try:
		t1 = e.type
	except AttributeError:
		e.type = do_check(e)

	return e.type



