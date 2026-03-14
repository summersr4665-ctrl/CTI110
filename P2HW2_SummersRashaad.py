# Rashaad Summers
# 03/14/2026
# P2HW2
# This program will ask the user to enter six module grades then store them in a list. It will display the lowest grade, highest grade, sum of grades, and average grade.


# ---------------- Pseudocode ----------------
# 1. Ask the user to enter grades for Module 1 through Module 6
# 2. Convert each grade to a float
# 3. Store all grades inside a list
# 4. Find the lowest grade using the min() function
# 5. Find the highest grade using the max() function
# 6. Find the sum of grades using the sum() function
# 7. Calculate the average by dividing the total by the number of grades
# 8. Display the results formatted neatly
# --------------------------------------------

# Get grades from user
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Create list to store grades
module_grades = [module1, module2, module3, module4, module5, module6]

# Calculate required values
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
grade_sum = sum(module_grades)
average_grade = grade_sum / len(module_grades)

# Display results
print("\n------------Results------------")

print(f"{'Lowest Grade:':20} {lowest_grade}")
print(f"{'Highest Grade:':20} {highest_grade}")
print(f"{'Sum of Grades:':20} {grade_sum}")
print(f"{'Average:':20} {average_grade:.2f}")

print("--------------------------------")
