"""Week 2 Homework: Exercises 1-11"""

import numpy as np
import matplotlib.pyplot as plt


# E1

# For our tic-tac-toe board, we will use a numpy array with dimension 3 by 3.
# Write a function create_board() that creates such a board with the value of each cell set to the integer 0.
# Call create_board() and store it.

def create_board():
    return np.zeros((3, 3), dtype=int)

board = create_board()
#print(board)


# E2

# Players 1 and 2 will take turns changing values of this array from a 0 to a 1 or 2, indicating the number of the player who places a marker there.
# Create a function place(board, player, position), where:
# - player is the current player (an integer 1 or 2).
# - position is a tuple of length 2 specifying a desired location to place their marker.
# Your function should only allow the current player to place a marker on the board (change the board position to their number) if that position is empty (zero).
# Use create_board() to store a board as board, and use place to have Player 1 place a marker on location (0, 0).

def place(board, player, position):
    pass