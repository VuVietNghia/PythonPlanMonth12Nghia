def math_interpreter():
    expression = input("Expression: ")

    x, operator, z = expression.split(" ")

    num1 = int(x)
    num2 = int(z)
    result = 0.0

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2

    print(f"Result: {result:.1f}")

math_interpreter()