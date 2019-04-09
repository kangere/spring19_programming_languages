from lang.expr import *



def eval_relational(e):
	if e.is_a(GtExpr):
		return evaluate(e.e1) > evaluate(e.e2)

	if e.is_a(LtExpr):
		return evaluate(e.e1) < evaluate(e.e2)

	if e.is_a(GteqExpr):
		return evaluate(e.e1) >= evaluate(e.e2)

	if e.is_a(LteqExpr):
		return evaluate(e.e1) <= evaluate(e.e2)
	
	if e.is_a(EqExpr):
		return evaluate(e.e1) == evaluate(e.e2)
	
	if e.is_a(NtEqExpr):
		return evaluate(e.e1) != evaluate(e.e2)

	raise TypeError("Relational expression exprected, actual: " + str(expr))


def eval_arithmetic(e):
	if e.is_a(AddExpr):
		return evaluate(e.e1) + evaluate(e.e2)

	if e.is_a(SubExpr):
		return evaluate(e.e1) - evaluate(e.e2)

	if e.is_a(MultExpr):
		return evaluate(e.e1) * evaluate(e.e2)

	if e.is_a(DivExpr):
		return evaluate(e.e1) / evaluate(e.e2)

	if e.is_a(RemExpr):
		return evaluate(e.e1) % evaluate(e.e2)
	
	raise TypeError("Arithmetic expression exprected, actual: " + str(expr))

def eval_logical(e):
	if e.is_a(AndExpr):
		return evaluate(e.e1) and evaluate(e.e2)

	if e.is_a(OrExpr):
		return evaluate(e.e1) or evaluate(e.e2)

	raise TypeError("Logical expression exprected, actual: " + str(expr))

def evaluate(expr):
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

	if expr.is_a(IntExpr):
		return expr.value

	if expr.is_a(NotExpr):
		return not evaluate(expr.e1)

	if expr.is_a(LogicalExpr):
		return eval_logical(expr)

	if expr.is_a(ArithmeticExpr):
		return eval_arithmetic(expr)

	

	raise Exception("Illegal state exception")
