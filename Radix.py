
#  File: Radix.py

#  Description: Given a list mixed of string with characters of digits and letters. Sort them
#  using queues. 

#  Student Name: Crystal Le

#  Student UT EID: cl44964

#  Partner Name: Johnny Tran

#  Partner UT EID: jht825

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created:03/27/2022

#  Date Last Modified: 03/28/2022

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Helper function to get the max number of passes that can be done from 
# length of longest string.
# Input: string a
# Output: max_len or max number of passes
def max_pass(a):
  sorted_lst = sorted(a, key=len)
  max_a = len(sorted_lst[-1])
  return max_a

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  qlst = [Queue() for i in range(38)]
  #add one / in for trailing in dictionary
  radix_dict = {'/': 0}

  for i in range(1, 38):
    if i <= 10:
      radix_dict[chr(47 + i)] = i
    else:
      radix_dict[chr(86 + i)] = i
  
  passes = max_pass(a) 

  #add trailing spaces to match length of longest string
  a_new = []
  for s in a:
    while len(s) < passes:
      s += '/'
    a_new.append(s)

  sorted_lst = a_new
  for n in range(-1, -(passes + 1), -1):

    # add all into queues
    for s in sorted_lst:
        qlst[radix_dict[s[n]]].enqueue(s)

    # dequeue and put into a new list
    sorted_lst = []
    for q in qlst:
      while not q.is_empty():       
        sorted_lst.append(q.dequeue())
  
  # replace trailing characters that filled in
  for b in range(len(sorted_lst)):
    sorted_lst[b] = sorted_lst[b].replace('/', '')
  
  return sorted_lst  

def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''
  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)
  
  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    