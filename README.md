# Bubble Sort Visualization
This is a Python program that visualizes the Bubble Sort algorithm for sorting an array of integers. The program uses the Pygame library to create a graphical interface and the pygame.mixer module to play sound effects during the sorting process.

# Installation
To run the program, you need to have Python 3 installed on your system, as well as the Pygame library. If you don't have Pygame installed, you can install it using pip by running the following command in your terminal:

```
pip install pygame
python tests.py
```

# Usage
When you run the program, a window will open showing a series of blue bars representing an array of random integers. The program will then run the Bubble Sort algorithm on the array, swapping adjacent elements that are in the wrong order until the array is sorted.

As the algorithm runs, you will hear a "swap" sound effect each time two elements are swapped. When the sorting is complete, you will hear a "success" sound effect, and the bars will turn green to indicate that the array is sorted.

You can modify the program to use a different number of bars or a different range of integers by changing the num_bars and bar_heights variables at the beginning of the code.

# Code Structure
The program consists of a bubble_sort function that implements the Bubble Sort algorithm, a draw_bars function that draws the array of bars on the screen, and a main loop that initializes the Pygame window and runs the sorting algorithm.

The bubble_sort function takes an array of integers as input and iterates over the array, swapping adjacent elements that are in the wrong order until the array is sorted. As each pair of elements is swapped, the draw_bars function is called to update the graphical representation of the array on the screen. The swap_sound effect is played each time a swap occurs.

The draw_bars function takes an array of integers as input and draws a series of blue bars on the screen to represent the array. When the sorted parameter is set to True, the bars are drawn in green to indicate that the array is sorted.

The main loop initializes the Pygame window and calls the draw_bars function to draw the initial array of bars. It then calls the bubble_sort function to sort the array, and waits for the user to close the window.

# Conclusion
This program provides a fun and interactive way to learn about the Bubble Sort algorithm and visualize how it works on an array of integers. By modifying the program and experimenting with different input sizes and ranges, you can gain a deeper understanding of how sorting algorithms work and how to optimize them for different use cases.
