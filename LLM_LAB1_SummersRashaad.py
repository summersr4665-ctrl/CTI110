#Rashaad Summers
#04/19/2026
#LLM_LAB1

# Simple Calculator Program with Input Validation, Looping, and Clean Output

# Function to safely get a number from the user
def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)   # Try converting to a number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    # Ask the user for two valid numbers
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    # Show the available operations
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get the user's choice
    choice = input("Enter the number of the operation you want (1-4): ")

    # Perform the chosen operation and format the output
    if choice == "1":
        result = num1 + num2
        symbol = "+"
        print(f"\n{num1} {symbol} {num2} = {result}")

    elif choice == "2":
        result = num1 - num2
        symbol = "-"
        print(f"\n{num1} {symbol} {num2} = {result}")

    elif choice == "3":
        result = num1 * num2
        symbol = "*"
        print(f"\n{num1} {symbol} {num2} = {result}")

    elif choice == "4":
        symbol = "/"
        if num2 == 0:
            print("\nError: You cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"\n{num1} {symbol} {num2} = {result}")

    else:
        print("\nInvalid choice. Please choose 1-4 next time.")

    # Ask if the user wants to calculate again
    again = input("\nDo you want to do another calculation? (yes/no): ").lower()

    if again != "yes":
        print("\nGoodbye!")
        break
