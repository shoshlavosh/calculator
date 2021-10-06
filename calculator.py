"""A calculator"""

from arithmetic import add, subtract, multiply, divide, square, cube, power, modulo

print("Hey, look! It's a calculator")

def menu():
    """Options for the calculator"""

    print("What would you like to do?")

    print("To ADD two numbers together, enter 'ADD'")
    print("To SUBTRACT one number from a second number, enter 'SUBTRACT'")
    print("To MULTIPLY two numbers, enter 'MULTIPLY'")
    print("To DIVIDE one number from another, enter 'DIVIDE")
    print("To SQUARE a number (multiply by itself twice), enter 'SQUARE'")
    print("To CUBE a number (multiply by itself 3 times), enter 'CUBE'")
    print("To calculate a number to the POWER of an exponent, enter 'POWER'")
    print("To get the REMAINDER of one number divided by another, enter 'REMAINDER'")
    print("To QUIT, enter 'Q' or 'QUIT'")

menu()

while True:

    #create while loop to continuously offer options to user
    #create options, including "quit"


    calculate = input("Choose an option, or to view all options, enter 'MENU': ")

    if calculate.lower() == "menu":
        menu()

    elif calculate.lower().startswith("q"):
        print()
        print("Thanks for calculating with us!")
        print("Goodbye!")
        break

    elif calculate.lower().startswith("a"):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        answer = add(num1, num2)

        print(f"{num1} added to {num2} equals {answer}.")

    elif calculate.lower().startswith("sub"):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        answer = subtract(num1, num2)

        print(f"{num2} subtracted from {num1} equals {answer}.")

    elif calculate.lower().startswith("mult"):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        answer = multiply(num1, num2)

        print(f"{num1} multiplied by {num2} equals {answer}.")

    elif calculate.lower().startswith("d"):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        answer = divide(num1, num2) #returns a float

        print(f"{num1} divided by {num2} equals {answer}.")

    elif calculate.lower().startswith("sq"):
        num = int(input("Enter a number: "))

        answer = square(num)

        print(f"{num} squared equals {answer}.")

    elif calculate.lower().startswith("c"):
        num = int(input("Enter a number: "))

        answer = cube(num)

        print(f"{num} cubed equals {answer}.")

    else:
        print("Sorry, that's not a valid option. Please try again.")

    

    



