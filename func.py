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

	if expr.is_a(BoolExpr):
		return 0;

	if expr.is_a(NotExpr):
		return 1 + height(expr.e1)

	if expr.is_a(BinaryExpr):
		return 1 + max([height(expr.e1), height(expr.e2)])

	raise Exception("Illegal state exception")



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

	if arg1.is_a(BoolExpr):
		return arg1.value == arg2.value

	if arg1.is_a(NotExpr):
		return same(arg1.e1,arg2.e1)

	if arg1.is_a(BinaryExpr):
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

	if expr.is_a(BoolExpr):
		return expr.value

	if expr.is_a(NotExpr):
		return not value(expr.e1)

	if expr.is_a(AndExpr):
		return value(expr.e1) and value(expr.e2)

	if expr.is_a(OrExpr):
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

	if expr.is_a(BoolExpr):
		return 1;

	if expr.is_a(NotExpr):
		return 1 + size(expr.e1)

	if expr.is_a(BinaryExpr):
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

	if expr.is_a(BoolExpr):
		return expr

	if expr.is_a(NotExpr):
		if expr.e1.is_a(BoolExpr):
			return BoolExpr(not value(expr.e1))
		else:
			return NotExpr(step(expr.e1))

	if expr.is_a(AndExpr):
		if not expr.e1.is_a(BoolExpr):
			return AndExpr(step(expr.e1), expr.e2)
		elif not expr.e2.is_a(BoolExpr):
			return AndExpr(expr.e1, step(expr.e2))
		else:
			return BoolExpr(value(expr))

	if expr.is_a(OrExpr):
		if not expr.e1.is_a(BoolExpr):
			return OrExpr(step(expr.e1), expr.e2)
		elif not expr.e2.is_a(BoolExpr):
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

	while not new_expr.is_a(BoolExpr):
		new_expr = step(new_expr)

	return new_expr


def resolve(e, env = []):

	if isinstance(e,IdExpr):
		for var in reversed(env):
			if e._id == var._name:
				e.ref = var
		return

	if isinstance(e,AbsExpr):
		env = env + [expr.var]
		resolve(e.expr,env)
		return 

	if isinstance(e,AppExpr):
		resolve(e.e1,env)
		resolve(e.e2,env)
		return 

def subst(e,s):
	assert isinstance(e,Expr), "Expression type required"
	
	if e.is_a(IdExpr):
		expr = s.get(e.ref)
		
		if expr is not None:
			return expr
		else
			return e

	if isinstance(e,AbsExpr):
		return AbsExpr(e.var,subst(e.expr,s))

	if isinstance(e,AppExpr):
		return AppExpr(subst(e.e1,s), subst(e.e2,s))
