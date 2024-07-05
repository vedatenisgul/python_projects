from art import logo
from os import system

def add(number1,number2):
    return number1 + number2

def substract(number1,number2):
    return number1 - number2

def multiply(number1,number2):
    return number1 * number2

def divide(number1,number2):
    return number1 / number2

operations = {"+":add,
              "-":substract,
              "*":multiply,
              "/":divide}
print(logo)

def calculator():
    number1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)

    while True:
        symbol = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))

        function = operations[symbol]
        result = function(number1,number2)
        print(f"{number1} {symbol} {number2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, type 'n' to start e new calculation, or type 'q' to exit: ")
        if choice == "q":
            return
        elif choice == "n":
            system("clear")
            calculator()
            return
        elif choice == "y":
            number1 = result
        else:
            print("Invalid choice!")
            return

calculator()
