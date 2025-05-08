from datetime import datetime

def calculate_total_age(age):
    current_year = datetime.now().year
    age = current_year - user_birth_year
    return age

user_birth_year = input('give birth year')
user_birth_year = int(user_birth_year)
age = calculate_total_age(user_birth_year)
print(age)
