from expr import *

def height(expr):
	"""
		Function computes height of an expression
		
		Paramters:
		expr (Expr): Expression whose height is to be computed

		Returns:
		int: Height of the expression
	"""
	assert isinstance(expr,Expr), "expr is not an expression, Expression type required"

	if isinstance(expr,BoolExpr):
		return 0;

	if isinstance(expr,NotExpr):
		return 1 + height(expr.e1)

	if isinstance(expr,BinaryExpr):
		return 1 + max([height(expr.e1), height(expr.e2)])

	raise Exception("Illegal state exception")


# not sure if same means equality of values or eqaulity of types
def same(arg1,arg2):
	"""
		Function checks if two expressions are identical

		Parameters:
		arg1,arg2 (Expr): Expressions to compare for equality

		Returns:
		bool: True if expressions are the same, else False
	"""
	assert isinstance(arg1,Expr), "arg1 is not an expression, Expression type required"
	assert isinstance(arg2,Expr), "arg2 is not an expression, Expression type required"
	
	if type(arg1) is not type(arg2):
		return False

	if isinstance(arg1,BoolExpr):
		return arg1.value == arg2.value

	if isinstance(arg1,NotExpr):
		return same(arg1.e1,arg2.e1)

	if isinstance(arg1,BinaryExpr):
		return same(arg1.e1,arg2.e1) and same(arg1.e2,arg2.e2)

	raise Exception("Illegal state exception")




def value(expr):
	"""
		Function computes the value of an expression

		Paramerter:
		expr (Expr): The whose value is to be computed

		Returns:
		bool: the value of the expression
	"""
	assert isinstance(expr,Expr), "expr is not an expression, Expression type required"

	if isinstance(expr,BoolExpr):
		return expr.value

	if isinstance(expr,NotExpr):
		return not value(expr.e1)

	if isinstance(expr,AndExpr):
		return value(expr.e1) and value(expr.e2)

	if isinstance(expr,OrExpr):
		return value(expr.e1) or value(expr.e2)

	raise Exception("Illegal state exception")


def size(expr):
	"""
		Fucntion computes size of an expression

		Parameter:
		expr (Expr): the expression whose size is to be computed

		Returns:
		int : size of the expression
	"""
	assert isinstance(expr,Expr), "expr is not an expression, Expression type required"

	if isinstance(expr,BoolExpr):
		return 1;

	if isinstance(expr,NotExpr):
		return 1 + size(expr.e1)

	if isinstance(expr,BinaryExpr):
		return 1 + size(expr.e1) + size(expr.e2)

	raise Exception("Illegal state exception")


def step(expr):
	"""
		Function retuns an expression representing a single step of evaluation
		
		Parameter:
		expr (Expr): the expression to step through

		Return:
		Expr: an expression reduced once
	"""
	assert isinstance(expr,Expr), "expr is not an expression, Expression type required"

	if isinstance(expr,BoolExpr):
		return expr

	if isinstance(expr,NotExpr):
		if isinstance(expr.e1,BoolExpr):
			return BoolExpr(not value(expr.e1))
		else:
			return NotExpr(step(expr.e1))

	if isinstance(expr,AndExpr):
		if not isinstance(expr.e1,BoolExpr):
			return AndExpr(step(expr.e1), expr.e2)
		elif not isinstance(expr.e2,BoolExpr):
			return AndExpr(expr.e1, step(expr.e2))
		else:
			return BoolExpr(value(expr))

	if isinstance(expr, OrExpr):
		if not isinstance(expr.e1,BoolExpr):
			return OrExpr(step(expr.e1), expr.e2)
		elif not isinstance(expr.e2,BoolExpr):
			return OrExpr(expr.e1, step(expr.e2))
		else:
			return BoolExpr(value(expr))

	raise Exception("Illegal state exception")


def reduce(expr):
	"""
		Function reduces expression till it is non reducible

		Parameter:
		expr (Expr): expression to reduce

		Return:
		Expr: reduced expression
	"""
	assert isinstance(expr,Expr), "expr is not an expression, Expression type required"

	new_expr = step(expr)

	while not isinstance(new_expr,BoolExpr):
		new_expr = step(new_expr)

	return new_expr

