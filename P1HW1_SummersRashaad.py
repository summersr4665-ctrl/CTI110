# Rashaad Summers
# 02/28/2026
# P1HW1
# Program collects user input, performs math, and displays results.

print("----- Calculating Exponents -----")

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print(base, "raised to the power of", exponent, "is", result, "!!")

print("\n----- Addition and Subtraction -----")

num1 = int(input("Enter starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

final_result = (num1 + num2) - num3

print(num1, "+", num2, "-", num3, "is equal to", final_result)