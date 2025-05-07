user_number = input('give a number')
user_number = int(user_number)

remainder = user_number % 2
if remainder == 0:
    print('even')
else:
    print('odd')
    