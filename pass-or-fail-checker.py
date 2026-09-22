#Write a program that asks for a student's score.

# Your program should:

# Accept a score from 0–100.
# If the score is 50 or above, print:
# Pass
# If the score is below 50, print:
# Fail


student_score   = int(input("Enter score:   "))

if student_score >= 50:
    print(f"Score:  {student_score}")
    print("Result:  Pass")

else:
    print(f"Score:  {student_score}")
    print("Result:  Fail")


