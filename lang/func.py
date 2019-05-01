from lang.expr import *
from lang.eval import *
from lang.type import *

def is_value(e):
	return type(e) in (IdExpr,AbsExpr,BoolExpr)

def is_reducible(e):
	return not is_value(e)


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

	if is_value(expr):
		return expr

	if expr.is_a(NotExpr):
		if expr.e1.is_a(BoolExpr):
			return BoolExpr(not evaluate(expr.e1))
		else:
			return NotExpr(step(expr.e1))

	if expr.is_a(AndExpr):
		if not expr.e1.is_a(BoolExpr):
			return AndExpr(step(expr.e1), expr.e2)
		elif not expr.e2.is_a(BoolExpr):
			return AndExpr(expr.e1, step(expr.e2))
		else:
			return BoolExpr(evaluate(expr))

	if expr.is_a(OrExpr):
		if not expr.e1.is_a(BoolExpr):
			return OrExpr(step(expr.e1), expr.e2)
		elif not expr.e2.is_a(BoolExpr):
			return OrExpr(expr.e1, step(expr.e2))
		else:
			return BoolExpr(evaluate(expr))

	if expr.is_a(AppExpr):
		return step_app(expr)

	raise Exception("Illegal state exception")


def step_app(e):

	if is_reducible(e.e1):
		return AppExpr(step(e.e1),e.e2)

	if not e.e1.is_a(AbsExpr):
		raise Exception("Lambda Expression expected, actual" + str(e.e1))


	if is_reducible(e.e2):
		return AppExpr(e.e1,step(e.e2))

	s = {
		e.e1.var : e.e2
	}
	return subst(e.e1,s)

def app_type(t):
	assert isinstance(t,AppType)

	if not isinstance(t.t1, AbsType):
		raise TypeError("type abstraction expected, found " + t.t1)

	if not isinstance(t.t1.expr.var,VarDecl):
		raise TypeError("Typed lambda expression expected")

	s = {
		t.t1.var : t.t2
	}
	return substType(t.t1,s)


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

	if e.is_a(IdExpr):
		for var in reversed(env):
			if e.id == var.name:
				e.ref = var
		return

	if e.is_a(NotExpr):
		resolve(e.e1,env)
		return

	if e.is_a(AbsExpr):
		env = env + [e.var]
		resolve(e.expr,env)
		return 

	if isinstance(e,AppExpr) or isinstance(e,BinaryExpr):
		resolve(e.e1,env)
		resolve(e.e2,env)
		return

	return




def subst(e,s):
	assert isinstance(e,Expr), "Expression type required"
	
	if e.is_a(IdExpr):
		if e.ref in s:
			return s[e.ref]
		else:
			return e

	if e.is_a(AbsExpr):
		return AbsExpr(e.var,subst(e.expr,s))

	if e.is_a(AppExpr):
		return AppExpr(subst(e.e1,s), subst(e.e2,s))

def substType(t,s):

	if isinstance(t,IdType):
		if t.name in s:
			return s[t.name]
		raise Exception("No member " + t.name)

	if isinstance(t,AbsType):
		newType = substType(t.expr.var.t,s)
		
		#rewrite type in lambda expressions
		newVar = VarDecl(t.expr.var.name,newType)

		#return substituted expression
		return AbsExpr(newVar,t.expr)
