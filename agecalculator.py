from datetime import datetime

birth_year = int(input("birth year: "))
current_year = datetime.now().year
approximate_age = current_year - birth_year
print(approximate_age)
