##############
# Calculator #
##############

print("It's time to use the calculator!\n")

def calculate(first_num, optr, next_num):
    if optr == "+":
        return first_num + next_num
    elif optr == "-":
        return first_num - next_num
    elif optr == "*":
        return first_num * next_num
    elif optr == "/":
        return first_num / next_num

first_number = int(input("What's the first number? \n"))
print()
print("+")
print("-")
print("*")
print("/")
print()
operation = input("Pick an operation: \n")
print()
next_number = int(input("What's the next number? \n"))
calculation = calculate(first_num = first_number, optr = operation, next_num = next_number)
print(calculation) # TEST CODE
# print("5 / 2 = 2.5")
# input("Type \"y\" to continue calculating with 2.5, or type \"n\" to start a new calculation: \n")

print()
print("Thanks for using the calculator!")