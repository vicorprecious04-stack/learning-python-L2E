# Student Result Management System
# Write a program that collects the names and scores of five students.

# Your program should:
# 1. Create two empty lists: names and scores.
# 2. Ask for each student's name and score.
# 3. Reject scores below 0 or above 100.
# 4. Store valid names and scores in their respective lists.
# 5. Display each student's name, score, grade, and pass/fail status.
# Grading rules:
# Score	Grade	Result
# 70–100	A	Pass
# 60–69	B	Pass
# 50–59	C	Pass
# 40–49	D	Fail
# 0–39	F	Fail


# Requirements:
# - Use lists and loops.
# - Use if, elif, and else.
# - A score of 50 or above is a pass.
# - Do not use external libraries.
# Tip: You can use one loop to collect the student information and another loop to calculate and display each student's result.
names = []
scores = []

for i in range(5):
    student_names = input(f"Enter name {i + 1}: ")
    student_score = int(input(f"Enter score {i + 1}: "))

    
    if 0 <= student_score <= 100:
        print("Invalid score")
        continue

    names.append(student_names)
    scores.append(student_score)

    
    if student_score >= 70:
        grade = "A"
    elif student_score >= 60:
        grade = "B"
    elif student_score >= 50:
        grade = "C"
    elif student_score >= 40:
        grade = "D"
    else:
        grade = "F"

    
    if grade in ("A", "B", "C"):
        result = "Pass"
    else:
        result = "Fail"

    print(f"Name: {student_names} | Score: {student_score} | Grade: {grade} | Result: {result}")

print(f"Names:  {names}")
print(f"Scores: {scores}")

