# : Age Eligibility Checker

# Write a program that asks the user to enter their age and determines their age category.

# Requirements
# Age	Output
# Below 0	Invalid age
# 0–12	Child
# 13–17	Teenager
# 18–59	Adult
# 60 and above	Senior Citizen

# Example 1
# Enter your age: 25
# You are an Adult.

Age = int(input("Enter your age:   "))
if Age < 0:
    print("Invalid age")

elif Age <= 12:
    print("You are a child")

elif Age <= 17:
    print("You are a Teenager") 

elif Age <= 59:
    print("You are an Adult")

else:
    print("You are a senior citizen")
