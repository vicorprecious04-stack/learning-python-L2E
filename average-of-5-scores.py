# Average of 5 Scores

# Write a program that asks the user for 5 scores.

# Your program must calculate and display:

# Total score
# Average score
# Example
# Enter score 1: 70
# Enter score 2: 80
# Enter score 3: 65
# Enter score 4: 90
# Enter score 5: 75

# Total: 380
# Average: 76.0
# Rules
# Use a for loop.
# Start your total at 0.
# Do not use Python's sum() function.
# Calculate the average yourself.

Total_score   = 0
Average_score   = 0
for i in range(1,6):
    scores  = int(input(f"Enter score {i}:   "))
    Total_score += scores

Average_score   = Total_score   / 5
print(f"Total score: {Total_score}")
print(f"Average score : {Average_score}")


