#write a program that displays a student score for maths, english and python

student_name    = input("Student:  ")
maths_score     = int(input("Mathematics:  "))
english_score   = int(input("English:  "))
python_score    = int(input("python:   "))

total   = maths_score   +   english_score   +   python_score    
average = total /   3
print(f"\n===== STUDENT RESULT =====  ")
print(f"Student name:   {student_name}")
print(f"maths score:    {maths_score}")
print(f"english score:  {english_score}")
print(f"Python score:   {python_score}")

print(f"Total:  {total}" )  
print(f"Average:    {average:.2f}")
print(f"==============================")