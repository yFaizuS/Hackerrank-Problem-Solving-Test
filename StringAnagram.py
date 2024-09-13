#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    # Step 1: Create a dictionary to count sorted string occurrences
    anagram_count = {}
    
    for word in dictionary:
        # Sort the word to create a key that represents all its anagrams
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_count:
            anagram_count[sorted_word] += 1
        else:
            anagram_count[sorted_word] = 1
    
    # Step 2: For each query, find the count of its anagram in the dictionary
    result = []
    for q in query:
        sorted_q = ''.join(sorted(q))  # Sort the query string
        result.append(anagram_count.get(sorted_q, 0))  # Append the count of anagrams
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
