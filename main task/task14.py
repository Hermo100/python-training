
num1 = None
num2 = None


while num1 is None:
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid character entered. Please enter a number or float.")


while num2 is None:
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid character entered. Please enter a number or float.")


result = num1 + num2
print("The sum of", num1,"and", num2, "is:", result)