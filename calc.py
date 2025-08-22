def add(x, y):
    return x + y

# Function to subtract two numbers


def subtract(x, y):
    return x - y

# Function to multiply two numbers


def multiply(x, y):
    return x * y

# Function to divide two numbers


def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

# Main loop to run the calculator


def calculator():
    print("Welcome to the simple calculator!")

    while True:
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Check if the choice is one of the valid operations
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {result}")
        else:
            print("Invalid choice! Please select a valid operation (1-5).")


if __name__ == "__main__":
    calculator()
