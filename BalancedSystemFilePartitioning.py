#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#

def mostBalancedPartition(parent, files_size):
    n = len(parent)
    
    # Step 1: Build an adjacency list to represent the tree
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[parent[i]].append(i)
    
    # Step 2: Calculate the total size of the entire tree
    total_size = sum(files_size)
    
    # Step 3: Perform DFS to calculate subtree sizes
    subtree_size = [0] * n
    
    def dfs(node):
        # Initially, the subtree size of the current node is its own file size
        subtree_size[node] = files_size[node]
        # Explore all children and accumulate their sizes
        for child in tree[node]:
            subtree_size[node] += dfs(child)
        return subtree_size[node]
    
    dfs(0)  # Start DFS from the root (node 0)
    
    # Step 4: Calculate the minimum difference
    min_diff = float('inf')
    for i in range(1, n):  # Don't cut the root
        subtree_sum = subtree_size[i]
        other_tree_sum = total_size - subtree_sum
        min_diff = min(min_diff, abs(subtree_sum - other_tree_sum))
    
    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    parent_count = int(input().strip())

    parent = []

    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)

    files_size_count = int(input().strip())

    files_size = []

    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)

    fptr.write(str(result) + '\n')

    fptr.close()
