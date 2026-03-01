# Rashaad Summers
# 03/01/2026
# P1HW2
# This program can calculate your travel expenses and show your remaining budget after expenses paid.

# Pseudocode:
# Ask user for budget
# Ask user for travel destination
# Ask user for gas cost
# Ask user for accommodation cost
# Ask user for food cost
# Add all expenses together
# Subtract total expenses from budget
# Display destination, expenses, and remaining balance

print("This program calculates travel expenses")

# Get user input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much will you spend on gas? "))
hotel = float(input("How much will you spend on accommodation? "))
food = float(input("How much will you spend on food? "))

# Calculate expenses
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

# Display results
print("\n------Travel Expenses------")
print("Location:", destination)
print("Initial Budget:", budget)
print("Fuel:", gas)
print("Accommodation:", hotel)
print("Food:", food)
print("Total Expenses:", total_expenses)
print("Remaining Balance:", remaining_balance)

