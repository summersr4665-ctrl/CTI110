# Rashaad Summers
# 03/14/2026
# P2HW1
# This program can calculate and displays travel expenses within a formatted table.

# Get user input
destination = input("Enter travel destination: ")
gas_cost = float(input("Enter amount you will spend on gas: "))
hotel_cost = float(input("Enter amount you will spend on accommodation: "))
food_cost = float(input("Enter amount you will spend on food: "))

# Calculate total cost
total_cost = gas_cost + hotel_cost + food_cost

# Display results
print("\n------------Travel Expenses------------")

print(f"{'Location:':20}{destination}")
print(f"{'Gas:':20}${gas_cost:,.2f}")
print(f"{'Accommodation:':20}${hotel_cost:,.2f}")
print(f"{'Food:':20}${food_cost:,.2f}")

print("---------------------------------------")
print(f"{'Total Expenses:':20}${total_cost:,.2f}")
