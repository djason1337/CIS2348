# Dominic Jason 2203959

birth_month = int(input('Enter birth month'))
birth_day = int(input('Enter birth day'))
birth_year = int(input('Enter birth year'))

current_month = int(input('Enter current month'))
current_day = int(input('Enter current day'))
current_year = int(input('Enter current year'))

age = (current_year - birth_year)

if current_month < birth_month and current_day < birth_day:
    age -= 1


print('Birthday Calculator')
print(f'Current date: {current_month}/{current_day}/{current_year}')
print(f'Birth date: {birth_month}/{birth_day}/{birth_year}')
print(f'You are {age} years old.')
if birth_month == current_month and birth_day == current_day:
    print("Happy birthday!")
