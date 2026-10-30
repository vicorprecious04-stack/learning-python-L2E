# Student Result Management System

# Write a program that collects the names and scores of five students.

# Your program should:

# Create two empty lists: names and scores.
# Ask for each student's name and score.
# Reject scores below 0 or above 100.
# Store valid names and scores in their respective lists.
# Display each student's name, score, grade, and pass/fail status.

# Grading rules:

# Score	Grade	Result
# 70–100	A	Pass
# 60–69	B	Pass
# 50–59	C	Pass
# 40–49	D	Fail
# 0–39	F	Fail

# Requirements:

# Use lists and loops.
# Use if, elif, and else.
# A score of 50 or above is a pass.
# Do not use external libraries.

# Tip: You can use one loop to collect the student information and another loop to calculate and display each student's result.

names = []
scores = []

while len(names) < 5:
    student_names = input(f"Enter name {len(names) + 1}: ")
    
    while True:
        try:
            student_scores = int(input(f"Enter score for {student_names}: "))
            if 0 <= student_scores <= 100:
                break
            else:
                print("Invalid score. Enter a valid score between 0 and 100.")
        except ValueError:
            print("Please enter a valid integer.")

    if student_scores >= 70:
        grade = "A"
    elif student_scores >= 60:
        grade = "B"
    elif student_scores >= 50:
        grade = "C"
    elif student_scores >= 40:
        grade = "D"
    else:
        grade = "F"

    result = "Pass" if grade in ("A", "B", "C") else "Fail"

    names.append(student_names)
    scores.append(student_scores)

    print(f"Name:   {student_names}")
    print(f"Score:  {student_scores}")
    print(f"Grade:  {grade}")
    print(f"Result: {result}")
    print("-" * 25)

print(f"Names:  {names}")
print(f"Scores: {scores}")


  