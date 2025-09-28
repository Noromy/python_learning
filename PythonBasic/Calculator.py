num1 = float(input("Enter a number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter another number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero!")
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid operator!")
