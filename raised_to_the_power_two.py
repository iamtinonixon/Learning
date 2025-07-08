def raise_to_the_power_two(to_the_power_two):
    power_two = user_number ** 2
    return power_two

user_number = input('give number')
user_number = int(user_number)
power_two = raise_to_the_power_two(user_number)
print(power_two)