# Rashaad Summers
# 04/05/2026
# P4LAB2
# A program that asks the user to enter an integer.

# Control variable for loop
run_again = "yes"

# While loop to keep program running
while run_again == "yes":

    # Get integer from user
    user_num = int(input("Enter an integer: "))

    # Check if number is negative
    if user_num < 0:
        print("This program does not handle negative values")

    else:
        # Display multiplication table using for loop
        for i in range(1, 13):
            result = user_num * i
            print(user_num, "x", i, "=", result)

    # Ask user if they want to run again
    run_again = input("Would you like to run the program again? (yes/no): ")

print("Program ended.")