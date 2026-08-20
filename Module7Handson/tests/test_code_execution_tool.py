from app.tools.code_execution_tool import execute_code


def test_code_execution():

    expressions = [
        "25 * 4",
        "100 / 5",
        "2 ** 5",
        "(10 + 5) * 2",
        "100 % 7",
        "__import__('os').system('dir')",
    ]

    for expression in expressions:

        result = execute_code(
            expression
        )

        print("\nExpression:")
        print(expression)

        print("Result:")
        print(result)


if __name__ == "__main__":
    test_code_execution()