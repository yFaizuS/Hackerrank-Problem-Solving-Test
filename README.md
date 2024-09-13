# Hackerrank-Problem-Solving-Test 

Questions:


1. Balanced System Files Partition
The directory structure of a system disk partition is represented as a tree. Its n directories are numbered from 0 to n-1, where the root directory has the number 0. The structure of the tree is defined by a parent array, where parent[i] = j means that the directory i is a direct subdirectory of j.
The value in files_size[i] denotes the sum of the sizes in kilobytes of the files located in directory i, but excluding its subdirectories. The size of the content of a directory is defined as the size of all files contained in this directory, plus the sum of the sizes of all of its subdirectories.
Partition the tree into two smaller ones by cutting one branch so that the sizes of the resulting subtrees are as close as possible.
Example:
parent = [-1, 0, 0, 1, 2, 2]
files_size = [1, 2, 2, 1, 1]
The structure of the system is shown in the diagram below. The nodes are labeled as <directory>/<file_size>.
Function Description:
Complete the function mostBalancedPartition in the editor below.
The function has the following parameters:
int parent[n]: each parent[i] is the parent directory of directory i
int files_size[n]: each files_size[i] is the sum of file sizes in directory i
Returns:
int: the minimum absolute difference in the size of content between two subtrees.

2. String Anagram
An anagram of a string is another string with the same characters in the same frequency, in any order. For example 'abc', 'bca', 'acb', 'bac', 'cba', 'tab' are all anagrams of the string 'abc'.
Given two arrays of strings, for every string in one list, determine how many anagrams of it are in the other list. Write a function that receives dictionary and query, two string arrays. It should return an array of integers where each element i contains the number of anagrams of query[i] that exist in dictionary.
Example:
dictionary = ['hack', 'a', 'rank', 'khac', 'ckh', 'kran', 'a', 'bb', 'ba', 'stairs', 'raits']
query = ["a", "nark", "bs", "hack", "stair"]
The final answer is [1, 2, 0, 3, 1].
