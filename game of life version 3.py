# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:33:01 2024

@author: janna
"""

import matplotlib.pyplot as plt
import numpy as np
import time
from copy import deepcopy

# Read data from the input file
my_file = open ("input.txt", "r")
data = my_file.read ()

my_file.close ()
data_splitted = data.strip().split("\n")

# Convert each character in the strings to integers and store in a 2D list (recent_data)
recent_data_splitted = [list(chain_char) for chain_char in data_splitted] 

# Initialize an empty list to store the converted data
recent_data = []

# Iterate over each string in the list recent_data_splitted
for chain_char in recent_data_splitted:
    # Convert each character in the string to an integer
    int_list = [int(char) for char in chain_char]
    
    # Add the list of integers to the recent_data list
    recent_data.append(int_list)

# print(recent_data)
 

# Function to count the number of live neighbors around a given cell
def nbre_neighbors_all(grid, i, j):
    nbre_col, nbre_row = np.shape(grid)
    nbre_neighbors = 0

    # Define the relative coordinates for neighboring cells
    neighbors_coords = [
        (-1, 0),  # North
        (1, 0),   # South
        (0, 1),   # East
        (0, -1),  # West
        (-1, 1),  # Northeast
        (-1, -1), # Northwest
        (1, 1),   # Southeast
        (1, -1)   # Southwest
    ]

    # Map relative coordinates to absolute indices and count neighbors with value 1
    nbre_neighbors = sum(grid[(i + x) % nbre_col, (j + y) % nbre_row] for x, y in neighbors_coords)

    return nbre_neighbors, neighbors_coords




# Function to calculate the next generation of the cellular automaton
def next_gen(grid):
    # Get the number of rows and columns in the input grid
    nbre_col = len(grid)
    nbre_row = len(grid[0])
    # Create a deep copy of the input grid to avoid modifying the original during calculations
    copy_grid = np.copy.deepcopy(grid)
    # Iterate over each cell in the grid, excluding the boundary cells
    for R in range(1, nbre_row - 1):
        if R == 0 or R == nbre_row:
            # Skip boundary rows
            continue
        else:
            for C in range(1, nbre_col - 1):
                # Iterate over each cell in the column, excluding the boundary cells
                for R_inter in range(1, nbre_row - 1):
                    # Check if the original cell is alive
                    if copy_grid[C][R] == 1: # Apply rules for live cells
                        if nbre_neighbors_all(grid, R_inter, C) == 1 or nbre_neighbors_all(grid, R_inter, C) == 2:
                            # Cell survives with 1 or 2 live neighbors
                            copy_grid[R_inter][C] = 1
                        else: # Cell dies due to overpopulation or underpopulation
                            copy_grid[R_inter][C] = 0
                    elif grid[R_inter][C] == 0: # Apply rules for dead cells
                        if nbre_neighbors_all(grid, R_inter, C) == 3:
                            # Dead cell comes to life with exactly 3 live neighbors
                            copy_grid[R_inter][C] = 1
    return copy_grid



#initialization
N = len(recent_data)
nbre_row, nbre_col = np.shape(recent_data)
array = [N - i for i in range(nbre_col)]
# Create an array with values decreasing from N-1 to 0
array = np.asarray([[line + column for column in range(nbre_col)] for line in range(nbre_row)])
# Create a 2D array (grid) where each cell contains the sum of its row and column indices
array2 = np.asarray([[line + column for column in range(nbre_col)] for line in range(nbre_row)])
# Create a temporary array with the same structure as 'array' to store the next generation
R = 0
C = 0



# Populate the array with initial values from the input data
for row in recent_data:
    for elt in row:
        array[C][R] = int(elt) # Convert character to integer and assign to the current cell
        R += 1
    C += 1
    R = 0



# Simulation loop
for i in range(3, 0, -1):
    plt.imshow(array)
    plt.pause(1)
    # Update each cell based on the rules of the cellular automaton
    for row in range(nbre_row):
        for col in range(nbre_col):
            # Calculate the number of live neighbors for the current cell
            neighbors = nbre_neighbors_all(array, row, col)
            # Apply the rules of the cellular automaton
            if array[row][col] == 1 and (neighbors == 2 or neighbors == 3):
                # Cell stays alive if it has 2 or 3 live neighbors
                array2[row][col] = 1
            elif array[row][col] == 0 and neighbors == 3:
                # Cell becomes alive if it has exactly 3 live neighbors
                array2[row][col] = 1
            else:
                # Cell dies or remains dead based on the rules
                array2[row][col] = 0
                
    # Update the array for the next generation
    array = deepcopy(array2)
    time.sleep(1)
    
    R=0
    C=0
