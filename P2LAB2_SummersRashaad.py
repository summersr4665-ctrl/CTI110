# Rashaad Summers
# 03/08/2026
# P2LAB2
# The use for this program is for a dictionary to store vehicle MPG values and calculate the gallons of gas that will be needed for a trip.



# Create dictionary with vehicle names and MPG values
car_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get all dictionary keys
keys = car_mpg.keys()

# Display available vehicles
print("Available vehicles:")
print(keys)
print()

# Ask user to enter a vehicle
vehicle = input("Enter a vehicle to see its MPG: ")
print()

# Display MPG of selected vehicle
mpg = car_mpg[vehicle]
print(f"The MPG for {vehicle} is {mpg}")
print()

# Ask user for miles to drive
miles = float(input("Enter the number of miles you will drive: "))
print()

# Calculate gallons needed
gallons_needed = miles / mpg

# Display result
print(f"You will need {gallons_needed:.2f} gallons of gas to drive the {vehicle}.")