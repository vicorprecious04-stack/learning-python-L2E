# Write a program that asks for a student's score and assigns a grade:

# Score	Grade
# 70–100	A
# 60–69	B
# 50–59	C
# 40–49	D
# Below 40	F

# Requirement: Use if, elif, and else.

student_score   = int(input("Enter score:   "))
if student_score < 0 or student_score > 100:
    print("Invalid input")
    

elif student_score >= 70:
    print("A")

elif student_score >= 60 :
    print("B") 

elif student_score  >= 50 :
    print("C")

elif student_score  >= 40 :
    print("D")

else:
    print("F")    
           