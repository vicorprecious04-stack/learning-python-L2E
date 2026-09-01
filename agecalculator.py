from datetime import datetime

birth_year = int(input("birth year: "))
current_year = datetime.now().year
approximate_age = current_year - birth_year
print(approximate_age)

#A more sophisticated one
from datetime import datetime
try:
    birth_year = int(input("birth year: "))

except ValueError:
    print("Please enter a valid year (numbers only).")  

else:

    current_year = datetime.now().year
    approximate_age = current_year - birth_year
    print(f"your approximate age is {approximate_age}.")