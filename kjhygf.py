try:
    num1 = int(input("Enter your first number "))
    num2 = int(input("Enter your second number "))
    operator =input("[*, +, /, - ] ")
except ValueError:
     print("you have entered an invalid input")
else:
    if operator == "*":
        print("Result is", num1 * num2)

    elif operator == "+":
        print("Result is", num1 + num2)
    elif operator == "-":
        print("Result is", num1 - num2)
    elif operator == "/":
        print("Result is", num1 / num2)
    else:
        print("you have enter incorrthect operator")

finally:
    print("Done")

