'''
How to use this Template:
For this assignment, do not change the function names or parameters
You will need to read from standard input. In order to do this, when 
you run your program in the command line, you will do it as follows:

$ python3 Intervals.py < intervals.in

If you read intervals.in as a file, it will not work on HackerRank. 
You should be able to paste this whole file into HackerRank. Please 
run your code to ensure it passes, and write your own test cases to 
ensure your answer is correct.
'''
#  File: Intervals.py

#  Description:

#  Student Name: Johnny Tran

#  Student UT EID: 

#  Partner Name: Crystal Le

#  Partner UT EID: 

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 1/27/2022

#  Date Last Modified: 
import sys
# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):
    merged_tuplst = []
    tuples_list = sorted(tuples_list)
    for i in tuples_list:
        if not merged_tuplst:
            merged_tuplst.append(i)
        else:
            j = merged_tuplst[-1]
            if i[0] - j[1] == 0:
                merged_tuplst[-1] = (j[0], i[1])
            elif i[0] <= j[1]:
                higher = max(j[1], i[1])
                merged_tuplst[-1] = (j[0], higher)
            else:
                merged_tuplst.append(i)
    return merged_tuplst



# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    for i in range(len(tuples_list) - 1):
        for j in range(i, len(tuples_list)):
            current = tuples_list[i][1] - tuples_list[i][0]
            next = tuples_list[j][1] - tuples_list[j][0]
            if next < current: 
                tuples_list[i], tuples_list[j] = tuples_list[j], tuples_list[i]
            elif current < next:
                tuples_list[i], tuples_list[j] = tuples_list[i], tuples_list[j]
            elif next == current:
                if tuples_list[i][0] < tuples_list[j][0]: 
                    tuples_list[i], tuples_list[j] = tuples_list[i], tuples_list[j]
                else: 
                    tuples_list[i], tuples_list[j] = tuples_list[j], tuples_list[i]
    return tuples_list
      




def main():
  # read the input data and create a list of tuples
  num_intervals = int(sys.stdin.readline())
  tup_lst = []
  for i in range(num_intervals):
    interval = sys.stdin.readline().split()
    interval[0] = int(interval[0])
    interval[1] = int(interval[1])
    tup_lst.append(tuple(interval))

  

  # merge the list of tuples
  #print(tup_lst)
  merged = merge_tuples(tup_lst)
  # print the merged list
  print(merged)
  # sort the list of tuples according to the size of the interval
  sorted = sort_by_interval_size(merged)
  # print the sorted list
  print(sorted)

if __name__ == "__main__":
   main()
