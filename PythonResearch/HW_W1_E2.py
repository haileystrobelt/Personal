"""Exercise 2:
Consider a circle inscribed in a square. The ratio of their areas (the ratio of the area of the circle to the area of the square) is π/4.
In this six-part exercise, we will find a way to approximate this value."""


import random
import math

# 2a
# Using the math library, calculate and print the value of π/4.
# What is the value of π/4?

def ratioArea():
    return math.pi/4

# 2b
# Using random.uniform(), create a function rand() that generates a single float between −1 and 1.
# Call rand() once. For us to be able to check your solution, we will use random.seed() to fix the seed value of the random number generator.


random.seed(1)  # Fixes the seed of the random number generator.
def rand():
    return random.uniform(-1,1)



# 2c
# The distance between two points x and y is the square root of the sum of squared differences along
# each dimension of x and y. Create a function distance(x, y) that takes two vectors and outputs the
# distance between them. Use your function to find the distance between (0,0) and (1,1).

def distance(x, y):
    dist = math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
    return dist



# 2d
# Write a function in_circle(x, origin) that determines whether a point in a two dimensional plane falls within a unit circle surrounding a given origin.
# Your function should return a boolean True if the distance between x and origin is less than 1 and False otherwise.
# Use distance(x, y) as defined in Exercise 2c.
# Use your function to determine whether the point (1,1) lies within the unit circle centered at (0,0)

def in_circle(x, origin = (0,0)):
    return distance(x, origin) < 1

#print(in_circle((1,1),(0,0)))


# 2e
# Create a list inside of R=10000 booleans that determines whether or not a point falls within the unit circle centered at (0,0).
# Set the seed to 1 using random.seed(1).
# Use the rand function from Exercise 2b to generate R randomly located points.
# Use the function in_circle to test whether or not a given point falls within the unit circle.
# Find the proportion of points that fall within the circle by summing all True values in the inside list; then divide the answer by R to obtain a proportion.
# Print your answer. This proportion is an estimate of the ratio of the two areas!
# What is the proportion of points within the unit circle?

R = 10000
#takes random points, creates 10000 (R) of them, then puts that list into a new list of whether they are inside the circle(True/False)
inside = [in_circle(point) for point in [(rand(), rand()) for i in range(R)]]
proportion = (sum(inside))/R
#print(proportion)

#2f
# Calculate the difference between your estimate from Exercise 2e and math.pi / 4. Note: inside and R are defined as in Exercise 2e.
# What is the difference between our estimate from 2e and the true value of π/4?

diff =  ratioArea() - proportion
#print(diff)