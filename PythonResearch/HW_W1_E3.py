"""Exercise 3:
A list of numbers representing measurements obtained from a system of interest can often be noisy.
One way to deal with noise to smooth the values by replacing each value with the average of the value and the values of its neighbors.
We will practice data smoothing in this three-part exercise."""

import random

random.seed(1)

# 3a
# Let's make a function moving_window_average(x, n_neighbors) that takes a list x and the number of neighbors
# n_neighbors on either side to consider. For each value, the function computes the average of each value's
# neighbors, including themselves. Have the function return a list of these averaged values that is the same
# length as the original list. If there are not enough neighbors (for cases near the edge), substitute the
# original value as many times as there are missing neighbors.
# Use your function to find the moving window sum of x=[0,10,5,3,1,5] and n_neighbors = 1.


def moving_window_average(x, n_neighbors = 1):

    # Add neighbors to the sides of list, the end values will be added repeatedly, depending on number of neighbors
    lst_len = len(x)
    x = [x[0]] * n_neighbors + x + [x[-1]] * n_neighbors
    width = n_neighbors * 2 + 1
    # this will put all the values, count sections of our list, depending on what the width was
    avg_vals = [sum(x[i:(i+width)]) / width for i in range(lst_len)]
    return avg_vals


#print(moving_window_average([0,10,5,3,1,5]))

# 3b
# Compute and store R=1000 random values from 0-1 as x.
# Compute the moving window average for x for values of n_neighbors ranging from 1 to 9 inclusive.
# Store x as well as each of these averages as consecutive lists in a list called Y.


def rand():
    return random.uniform(0,1)


R = 1000

x = [rand() for i in range(R)]
n_neighbors = range(1,10)


Y = [x] + [moving_window_average(x, n) for n in n_neighbors]
#10th entry in x if n_neighbors is 5
#print(moving_window_average(x, 5)[9])


# 3c
# For each list in Y, calculate and store the range (the maximum minus the minimum) in a new list ranges.
# Print your answer

ranges = [max(x)-min(x) for x in Y]
#print(ranges)




