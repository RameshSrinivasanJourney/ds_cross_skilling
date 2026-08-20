import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def execute_code(expression: str) -> dict:
    """
    Safely evaluate a mathematical expression.

    Only numeric expressions and supported
    mathematical operators are allowed.
    """

    try:
        tree = ast.parse(
            expression,
            mode="eval"
        )

        result = _evaluate(tree.body)

        return {
            "expression": expression,
            "result": result,
        }

    except Exception as exc:
        return {
            "expression": expression,
            "error": str(exc),
        }


def _evaluate(node):

    if isinstance(node, ast.Constant):

        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError(
            "Only numeric values are allowed."
        )

    if isinstance(node, ast.BinOp):

        left = _evaluate(node.left)
        right = _evaluate(node.right)

        operator_function = OPERATORS.get(
            type(node.op)
        )

        if operator_function is None:
            raise ValueError(
                "Unsupported operator."
            )

        return operator_function(
            left,
            right
        )

    if isinstance(node, ast.UnaryOp):

        operand = _evaluate(node.operand)

        operator_function = OPERATORS.get(
            type(node.op)
        )

        if operator_function is None:
            raise ValueError(
                "Unsupported unary operator."
            )

        return operator_function(
            operand
        )

    raise ValueError(
        "Only mathematical expressions are allowed."
    )