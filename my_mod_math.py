# my_mod_math.py

import math

# Function to calculate the volume of a sphere with a given radius
def volume_of_sphere(radius):
    return (4/3) * math.pi * radius**3

# Function to calculate the area of a triangle with given sides using Heron's formula
def area_of_triangle(side_a, side_b, side_c):
    # Calculate the semi-perimeter
    s = (side_a + side_b + side_c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    return area

# Function to calculate the factorial of a number
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# Function to find the nth number in the Fibonacci sequence
def fibonacci(n):
    n = n + 1
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]

# Function to find the greatest common divisor (gcd) of two numbers
def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
