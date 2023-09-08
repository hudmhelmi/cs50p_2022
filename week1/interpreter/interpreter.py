expression = input("Expression: ")
expression = expression.split(" ")
if expression[1] == "+":
    print(float(expression[0]) + float(expression[2]))
elif expression[1] == "-":
    print(float(expression[0]) - float(expression[2]))
elif expression[1] == "*":
    print(float(expression[0]) * float(expression[2]))
elif expression[1] == "/":
    print(float(expression[0]) / float(expression[2]))