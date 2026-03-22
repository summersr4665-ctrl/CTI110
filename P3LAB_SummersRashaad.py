# Name: Rashaad Summers
# Date: 03/22/2026
# Assignment: P3LAB
# Description: This program will calculate the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money.

# Step 1: Get user input
money = float(input("Enter a money value (ex: 5.67): "))

# Step 2: Convert to cents (integer)
total_cents = int(money * 100)

# Step 3: Calculate dollars
dollars = total_cents // 100
remaining = total_cents - (dollars * 100)

# Step 4: Calculate quarters
quarters = remaining // 25
remaining = remaining - (quarters * 25)

# Step 5: Calculate dimes
dimes = remaining // 10
remaining = remaining - (dimes * 10)

# Step 6: Calculate nickels
nickels = remaining // 5
remaining = remaining - (nickels * 5)

# Step 7: Remaining pennies
pennies = remaining

# Step 8: Display results

print("\nChange breakdown:")

# Dollars
if dollars > 0:
    if dollars == 1:
        print("1 Dollar")
    else:
        print(dollars, "Dollars")

# Quarters
if quarters > 0:
    if quarters == 1:
        print("1 Quarter")
    else:
        print(quarters, "Quarters")

# Dimes
if dimes > 0:
    if dimes == 1:
        print("1 Dime")
    else:
        print(dimes, "Dimes")

# Nickels
if nickels > 0:
    if nickels == 1:
        print("1 Nickel")
    else:
        print(nickels, "Nickels")

# Pennies
if pennies > 0:
    if pennies == 1:
        print("1 Penny")
    else:
        print(pennies, "Pennies")

