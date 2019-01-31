from expr import *

def height(expr):
	"""
		Function computes height of an expression
		
		Paramters:
		expr (Expr): Expression whose height is to be computed

		Returns:
		int: Height of the expression
	"""
	assert isinstance(expr,Expr), "Expression type required"

	if isinstance(expr,BoolExpr):
		return 0;

	if isinstance(expr,NotExpr):
		return 1 + height(expr.e1)

	if isinstance(expr,BinaryExpr):
		return 1 + max([height(expr.e1), height(expr.e2)])


def same(e1,e2):
	"""
		Function checks if two expressions are identical

		Parameters:
		e1,e2 (Expr): Expressions to compare for equality

		Returns:
		bool: True if expressions are the same, else False
	"""
	return value(e1) == value(e2)

def value(expr):
	"""
		Function computes the value of an expression

		Paramerter:
		expr (Expr): The whose value is to be computed

		Returns:
		bool: the value of the expression
	"""
	assert isinstance(expr,Expr), "Expression type required"

	if isinstance(expr,BoolExpr):
		return expr.value

	if isinstance(expr,NotExpr):
		return not value(expr.e1)

	if isinstance(expr,AndExpr):
		return value(expr.e1) and value(expr.e2)

	if isinstance(expr,OrExpr):
		return value(expr.e1) or value(expr.e2)