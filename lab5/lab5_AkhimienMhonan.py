"""
Efuah Akhimien-Mhonan
Feb 5, 2026
Lab 5, Function
"""

import math
from lab5_function_AkhimienMhonan import *

print('\n---- Example 1: user-defined function')

w = 8
length = 3
a = area_rectangle(w, length)
print_area_result(w, length, a)


print('\n---- Example 2: calculate the distance of two points')

x1 = collectnum('x1')
x2 = collectnum('x2')
y1 = collectnum('y1')
y2 = collectnum('y2')

# testing
# print(f"({x1},{y1}) ({x2},{y2})")

# testing
# print(f"distance = {calculate_distance(x1,x2,y1,y2)}")

distance = calculate_distance(x1, x2, y1, y2)
print_distance(x1, x2, y1, y2, distance)


print('\nEXERCISE')

import random

# function that generates and returns a random number between min and max
def generate_random(min_num, max_num):
    return random.randint(min_num, max_num)

# function that compares the guess number with the random number
def compare_guess(random_number):
    GUESS_NUMBER = 5   # constant guess number

    if random_number < GUESS_NUMBER:
        print("The number is smaller than the guess number")
    elif random_number > GUESS_NUMBER:
        print("The number is bigger than the guess number")
    else:
        print("You got it!")

# calling the functions
rand_num = generate_random(1, 10)
print(f"Random number generated: {rand_num}")
compare_guess(rand_num)
