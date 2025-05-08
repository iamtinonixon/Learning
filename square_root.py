def give_square_root(square):
    square_root = user_number ** 2
    return square_root

user_number = input('give number')
user_number = int(user_number)

square_root = give_square_root(user_number)
print(square_root)