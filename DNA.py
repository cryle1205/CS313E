
#  File: DNA.py

#  Description:

#  Student Name: Crystal Le

#  Student UT EID: 

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 01/19/2022

#  Date Last Modified:

import sys #system 

# Input: string s
# Output: returns a list of all substrings of s

def all_substrs(s):
  #create a list to store the substrings
  substr_list = []

  #get the size of the window
  window = len(s)

  #find all substrings
  while (window > 0):
    start_index = 0
    while((start_index + window) <=len(s)):
      sub_string = s[start_index: start_index + window]
      substr_list.append(sub_string)
      start_index +=1
    window -= 1
  return substr_list
# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.
def longest_subsequence (s1, s2):
  #did not use this function
  longest_seq = []
  short_seq = []
  same_len = []
  if len(s1) > len(s2):
    longest_seq.append(s1)
    short_seq.append(s2)
    return longest_seq, short_seq
  elif len(s1) < len(s2):
    longest_seq.append(s2)
    short_seq.append(s1)
    return longest_seq, short_seq
  else:
    same_len.append(s1)
    same_len.append(s2)
    return same_len
  
print()
def main():
  # read the number of pairs
  num_pairs = sys.stdin.readline() #stdin is a function that reads from the console
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)

  
  # for each pair call the longest_subsequence
  for i in range (num_pairs):
    st1 = sys.stdin.readline()
    st2 = sys.stdin.readline()

    st1 = st1.strip()
    st2 = st2.strip()

    st1 = st1.upper()
    st2 = st2.upper()

    # get the longest subsequences
    long_sub = longest_subsequence (st1, st2)
    substr_list1 = all_substrs(st1)
    substr_list2 = all_substrs(st2)
    #print(substr_list1)
    #print(substr_list2)
    
    # print the result
    max_len1 = 0 
    max_len2 = 0
    if len(substr_list1) > len(substr_list2):
      max_len1 = len(substr_list1)
    elif len(substr_list1) < len(substr_list2):
      max_len2 = len(substr_list2)
    else:
      max_len1 = len(substr_list1)
    
    lcs_list = []
    if max_len1 != 0:
      for i in range(max_len1-1):
        if substr_list1[i] in substr_list2: 
          lcs_list.append(substr_list1[i])
    
    if max_len2 != 0:
      for i in range(max_len2-1):
        if substr_list2[i] in substr_list1: 
          lcs_list.append(substr_list2[i])

    
    longest_sub = sorted(lcs_list, key = len)
    # if len(longest_sub) > 1:
    #   print(longest_sub[-1])
    #   if len(longest_sub[-1]) == len(longest_sub[-2]):
    #     print(longest_sub[-2])
    # else:
    #   print("No Common Sequence Found")

    max_lcs = 0
    if len(longest_sub) > 1:
      max_lcs = len(longest_sub[-1])
      longest_sub =sorted(longest_sub)
      for sub in longest_sub:
        if len(sub) == max_lcs:
          print(sub)
    else:
      print("No Common Sequence Found")
    # insert blank line
    print()
    
if __name__ == "__main__":
  main()

#def test_cases():
  #test the function longest_subsequence()
  #assert longest_subsequence("", "") == []
  #assert longest_subsequence("abcd", "abcd") == ["abcd"]
  #assert longest_subsequence("abcd", "bcef") == ["bc"]
  #assert longest_subsequence("abcd", "xyz") == []

  #return "all test cases passed"
