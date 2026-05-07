# Rashaad Summers
# 04/26/2026
# P5LAB
# This program will simulate a customer using a self-checkout machine. 
import random

# Function to display change
def disperse_change(money):

    # Convert money to cents
    total_cents = int(round(money * 100))

    # Calculate dollars
    dollars = total_cents // 100
    remaining = total_cents % 100

    # Calculate quarters
    quarters = remaining // 25
    remaining = remaining % 25

    # Calculate dimes
    dimes = remaining // 10
    remaining = remaining % 10

    # Calculate nickels
    nickels = remaining // 5
    remaining = remaining % 5

    # Remaining pennies
    pennies = remaining

    print()

    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(dollars, "Dollars")

    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(quarters, "Quarters")

    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(dimes, "Dimes")

    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(nickels, "Nickels")

    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(pennies, "Pennies")


# Main function
def main():

    # Generate random amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)

    print("You owe $" + format(amount_owed, ".2f"))

    # Ask user for cash amount
    cash = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change
    change = round(cash - amount_owed, 2)

    print("Change is: $" + format(change, ".2f"))

    # Call function
    disperse_change(change)


# Call main
main()