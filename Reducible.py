#  File: Reducible.py

#  Description: This program will remove a letter at a time but they'll still be a new word. It will then return the largest reducible word.

#  Student's Name: Johnny Tran

#  Student's UT EID: jht825

#  Partner's Name: Crystal Le

#  Partner's UT EID: cl44964

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/23/22

#  Date Last Modified: 3/25/2022

import sys
# # Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
    if (n == 1):
        return False
    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True


# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    return const - hash_word(s, const)


# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    idx = hash_word(s, len(hash_table))

    if hash_table[idx] == '':
        hash_table[idx] = s
    else:
        step = step_size(s, 13)
        num_steps = 1
        while hash_table[(idx + step * num_steps) % len(hash_table)] != '':
            num_steps += 1
        hash_table[(idx + step * num_steps) % len(hash_table)] = s
    


# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    idx = hash_word(s, len(hash_table))

    if hash_table[idx] == s:
        return True

    elif hash_table[idx] != '':
        step = step_size(s, 13)
        num_steps = 1
        while hash_table[(idx + step * num_steps) % len(hash_table)] != '':
            if hash_table[(idx + step * num_steps) % len(hash_table)] == s:
                return True
            num_steps += 1
    return False


# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    if len(s) == 1:
        return s == "a" or s =="i" or s =="o"
    
    elif find_word(s, hash_memo):
        return True
        
    elif not find_word(s, hash_table):
        return False

    else:
        short_words_lst = get_short_words(s, hash_table)
        for word in short_words_lst:
            if is_reducible(word, hash_table, hash_memo):
                insert_word(word, hash_memo)
                return True
      
      
# helper function
# Input: string s, hash table
# Output: finds smaller words within the word and takes it and puts in a list to return to 
# is_reducible for entering to hash memo      
def get_short_words(s, hash_table):
    short_words_lst = []
    for i in range(len(s)):
        stored = s[:]
        if find_word(stored[:i] + stored[i + 1:], hash_table):
            short_words_lst.append(stored[:i] + stored[i + 1:])
    return short_words_lst


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    longest = []
    sorted_lst = sorted(string_list, key=len)
    max_len = len(sorted_lst[-1])
    
    for word in string_list:
        if len(word) == max_len:
            longest.append(word)
    return longest


def main():
    # create an empty word_list
    word_list = []

   # read words from words.txt and append to word_list
    for line in sys.stdin:
        line = line.strip()
        word_list.append (line)

    # Add smallest possible words!!
    word_list.append("i")
    word_list.append("a")
    word_list.append("o")

    # find length of word_list
    length_words = len(word_list)
     # determine prime number N that is greater than twice
    # the length of the word_list
    N = (2 * length_words) + 1
    while not is_prime(N):
        N += 1
    
    # create an empty hash_list
    hash_list = []

    # populate the hash_list with N blank strings
    for i in range(N):
        hash_list.append('')

    # hash each word in word_list into hash_list for collisions use double hashing .
    for word in word_list:
        # Put into hash table
        insert_word (word, hash_list)

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than 
    # 0.2 * size of word_list
    M = (0.2 * len(word_list)) + 1
    while not is_prime(M):
        M += 1
    
    # populate the hash_memo with M blank strings
    hash_memo = []
    for i in range(int(M)):
      hash_memo.append('')

    # create an empty list reducible_words
    reducible_words = []
    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)

    # find words of length 10 in reducible_words
    max_ls = get_longest_words(reducible_words)


    # print the words of length 10 in alphabetical order
    # one word per line
    for word in sorted(max_ls):
        print(word)

if __name__ == "__main__":
    main()
