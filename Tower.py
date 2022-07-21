#  File: Tower.py

#  Description: Similar to the Hanoi Towers, we now are trying to move n disks
#  using 4 pegs with k discs minimizing the number of moves. 

#  Student's Name: Crystal Le

#  Student's UT EID: CL44964

#  Partner's Name: Johnny Tran

#  Partner's UT EID: JHT825

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 03/05/2022

#  Date Last Modified: 03/07/2022

import sys, math
# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
  k = math.ceil(n - (2 * n + 1)**0.5 + 1)
  if (n == 0):
    return 0
  elif (n == 1):
    return 1
  else:
    return 2 * num_moves(k -1) + (2 * (2**(n - k) - 1)) + 1
  

def main():
  # read number of disks and print number of moves
  for line in sys.stdin:
    line = line.strip()
    num_disks = int (line)
    print (num_moves (num_disks))

if __name__ == "__main__":
  main()

