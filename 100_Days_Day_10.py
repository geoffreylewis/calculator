##############
# Calculator #
##############

# ASCII art for beginning banner/logo (courtesy of https://replit.com/@appbrewery/calculator-start#art.py).
# Slight modification by author.
banner_logo = """
 _____________________
|  _________________  |
| | PythonCalc   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# Intro to the calculator.
print(banner_logo)
print("It's time to use the calculator!\n")

# Defining the mathematical operations.
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

# Dictionary that holds the operational functions.
operational_functions = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

# Pick your first number.
number_1 = int(input("What's the first number? \n"))
print()

# Display possible operations.
for optr in operational_functions:
    print(optr)
print()

# Pick an operation.
operation = input("Pick an operation: \n")
print()

# Pick your second number.
number_2 = int(input("What's the next number? \n"))
print()

# Calculating the initial solution.
initial_calculation = operational_functions[operation] # Use the dictionary above.
initial_answer = initial_calculation(number_1, number_2) # Pass in your arguments/numbers.
print("It looks like: ")
print(f"{number_1} {operation} {number_2} = {initial_answer}") # Print the above choices and answer.
print()

continue_calculating = str(input("Type \"y\" to continue calculating with 2.5, or type \"n\" to start a new calculation: \n").lower())

# The end of calculations.
print()
print("Thanks for using the calculator!")