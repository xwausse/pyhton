def square(a):
    perimeter = 4 * a
    area = a * a   
    return perimeter, area

print(square(5)) 


import math

def circle_length(d):
    return math.pi * d

print(circle_length(10))

def mean(a, b):
    return (a + b) / 2

print(mean(4, 8))

def numbers_info(a, b):
    summ = a + b
    product = a * b
    square_a = a ** 2
    square_b = b ** 2
    return summ, product, square_a, square_b

print(numbers_info(3, 5)) 
