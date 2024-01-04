# Calculator Program

# Function to perform addition
def add(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# Function to perform division
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero."

# Main program
print("Welcome to the Calculator Program!")
print("Please select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    result = add(num1, num2)
    print("The result of addition is:", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("The result of subtraction is:", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("The result of multiplication is:", result)
elif choice == '4':
    result = divide(num1, num2)
    print("The result of division is:", result)
else:
    print("Invalid choice. Please select a number between 1 and 4.")
