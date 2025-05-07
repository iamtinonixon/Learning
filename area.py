def calculate_area_of_a_circle(radius):
    area = pi * radius ** 2 
    return area

pi = 3.14
r = input('input radius')
r = float(r)
area = calculate_area_of_a_circle(r)
print(area)
 
