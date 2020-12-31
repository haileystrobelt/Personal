import random
import math

random.seed(1)  # Fixes the seed of the random number generator.


def rand():
    print(random.uniform(-1,1))

    # 2c
    # The distance between two points x and y is the square root of the sum of squared differences along
    # each dimension of x and y. Create a function distance(x, y) that takes two vectors and outputs the
    # distance between them. Use your function to find the distance between (0,0) and (1,1).
    # Print your answer.
def distance(x, y): #x,y are points
    dist = math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def in_circle(x, origin = [0,0]):
   pass

# define `rand` here!

rand()