# Rashaad Summers
# 04/12/2026
# P4HW1
# Instead of an individual statement to collect each score, the program will use a loop. Also, after displaying score average (after dropping lowest score) , the program is to display a letter grade for the calculated average.

# Pseudocode / Algorithm
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list to store the scores.
# 3. Use a loop to collect each score.
# 4. For each score entered:
#    a. Check if the score is valid (between 0 and 100).
#    b. If the score is not valid, display an error message.
#    c. Keep asking until a valid score is entered.
#    d. Add the valid score to the list.
# 5. Find the lowest score in the list.
# 6. Remove the lowest score from the list.
# 7. Find the average of the modified list.
# 8. Determine the letter grade based on the average.
# 9. Display the results:
#    - Lowest score
#    - Modified score list
#    - Average score
#    - Letter grade

# Ask user for number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Create empty list for scores
score_list = []

# Loop to collect scores
for score_num in range(1, num_scores + 1):
    score = float(input(f"Enter score #{score_num}: "))

    # Validate score
    while score < 0 or score > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_num} again: "))

    # Add valid score to list
    score_list.append(score)

# Find lowest score
lowest_score = min(score_list)

# Remove lowest score from list
score_list.remove(lowest_score)

# Calculate average
score_average = sum(score_list) / len(score_list)

# Determine letter grade
if score_average >= 90:
    letter_grade = "A"
elif score_average >= 80:
    letter_grade = "B"
elif score_average >= 70:
    letter_grade = "C"
elif score_average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print()
print("------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {score_average:.2f}")
print(f"Grade         : {letter_grade}")
print("--------------------------------")