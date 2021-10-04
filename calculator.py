"""A calculator"""

from arithmetic import add, subtract, multiply, divide, square, cube, power, modulo

print("Hey, look! It's a calculator")

print("What would you like to do?")

print("To add two numbers together, enter 'Add': ")

calculate = input("Choose an option: ")

if calculate.lower() == "add":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    answer = add(num1, num2)

    print(f"The answer is {answer}.")


