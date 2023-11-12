#build a calculator (using function):

num1 = float(input("Enter the first number: \n"))
ops = input("Enter an operator (+, -, *, /): \n")
num2 = float(input("Enter the second number: \n"))

def calculator(num1, num2):
    if ops == "+":
        print(num1 + num2)
    elif ops == "-":
        print(num1 - num2)
    elif ops == "*":
        print(num1 * num2)
    elif ops == "/":
        print(num1 / num2)
    else:
        print("You have invalid input. Please check.")
# !!! remember to call the function to "activate" it.
calculator(num1, num2)