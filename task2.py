# Calculator Program
print("Simple Calculator")
print("Operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
choice = input("Enter operation (+, -, *, /): ")

# Performing the calculation
if choice == '+':
    result = num1 + num2
elif choice == '-':
    result = num1 - num2
elif choice == '*':
    result = num1 * num2
elif choice == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

# Displaying the result
print("Result:", result)
