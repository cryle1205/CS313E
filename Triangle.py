#  File: Triangle.py

#  Description: This program will take in a triangle of numbers
#  and show the maximum path sum using 4 different algorithms.

#  Student's Name: Johnny Tran

#  Student's UT EID: 

#  Partner's Name: Crystal Le

#  Partner's UT EID: 

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/3/2022

#  Date Last Modified:3/4/2022

import sys

from timeit import timeit


# returns the greatest path sum using exhaustive search
def brute_force(grid):
    total = []
    brute_force_helper(grid, 0, 0, total, 0)
    return max(total)


def brute_force_helper(grid, row, col, total, i):
    # total collects the sum of every path taken with the brute force method.
    if row == len(grid):
        return total.append(i)
    else:
        return brute_force_helper(grid, row + 1, col, total,
                                  i + grid[row][col]) or brute_force_helper(
            grid, row + 1, col + 1, total, i + grid[row][col])


# returns the greatest path sum using greedy approach
def greedy(grid):
    total = grid[0][0]
    j = 0
    # checks to see if the position is greater than the current position. If it is then we can take the value of the new position.
    for i in range(1, len(grid)):
        if grid[i][j + 1] > grid[i][j]:
            j += 1
        total += grid[i][j]
    return total


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    return divide_conquer_helper(grid, 0, 0)


def divide_conquer_helper(grid, row, col):
    # will return the value at the very end.
    if row == len(grid) - 1:
        return grid[row][col]
    # continues to go down the triangle but adds the first and the max together every time the recursion is called.
    else:
        return grid[row][col] + max(divide_conquer_helper(grid, row + 1, col), divide_conquer_helper(grid, row + 1, col + 1))


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    # begins at the second to last tow and the second for loop will go through all col and add the max to whichever is larger.
    for i in range(len(grid) - 2, -1, -1):
        for j in range(i + 1):
            grid[i][j] += max(grid[i + 1][j], grid[i + 1][j + 1])
    # returns the top of grid because the max will eventually be at the top.
    return grid[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    '''
  # check that the grid was read in properly
  print (grid)
  '''

    # output greatest path from exhaustive search
    times = timeit('brute_force({})'.format(grid),
                   'from __main__ import brute_force', number=10)
    times = times / 10
    # print time taken using exhaustive search

    # output greatest path from greedy approach
    times = timeit('greedy({})'.format(grid), 'from __main__ import greedy',
                   number=10)
    times = times / 10
    # print time taken using greedy approach

    # output greatest path from divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(grid),
                   'from __main__ import divide_conquer', number=10)
    times = times / 10
    # print time taken using divide-and-conquer approach

    # output greatest path from dynamic programming
    times = timeit('dynamic_prog({})'.format(grid),
                   'from __main__ import dynamic_prog', number=10)
    times = times / 10
    # print time taken using dynamic programming


if __name__ == "__main__":
    main()
