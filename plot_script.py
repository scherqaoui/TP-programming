# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:12:18 2023

@author: SALMA
"""

      
import random as rd
import matplotlib.pyplot as plt
import numpy as np
import sys

# Task 3






if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('missing input. please provide numerical ')
    
    value = int(sys.argv[1])

    # Task 1
    def random_number(N):
        N_rd_nbr = []
        for i in range(N):
            N_rd_nbr.append(rd.random())
        return N_rd_nbr

    rand_numbers = random_number(value)

    # Task 2
    def graphics(my_rand_numbers):
        
        indices = list(range(len(my_rand_numbers)))
        # Create a list of indices to be used as x-axis values for the plots
        
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
         # Create subplots with three different types of plots
        
        ax1.plot(indices, my_rand_numbers)
        ax1.set_title('graph of $(n,x_n)$')
        # Line plot
        
        ax2.scatter(my_rand_numbers[1:], my_rand_numbers[:-1])
        ax2.set_title('scatter plot fo the points $(x_n, x_{n-1})$')
        # Scatter plot of consecutive points
        
        ax3.hist(np.array(my_rand_numbers))
        ax3.set_title('histogram of the distribution')
        # Histogram of the distribution
        
        
        plt.show()  # Display the plots before exiting

    graphics(rand_numbers) # Call the graphics function with the generated random numbers
    sys.exit()





       
   
































































