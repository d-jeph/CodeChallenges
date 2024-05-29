"""
Given the root of a binary tree, find the most frequent subtree sum. 
The subtree sum of a node is the sum of all values under a node, including the node itself.
"""

from collections import Counter
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        """
        Find all subtree sums that occur the most frequently in the binary tree.
      
        :param root: TreeNode, the root of the binary tree
        :return: List[int], a list of most frequent subtree sums
        """
      
        def dfs(node):
            """
            Perform a depth-first search to calculate the sum of each subtree.
          
            :param node: TreeNode, the current node in the binary tree
            :return: int, the sum of the current subtree
            """
            if not node:
                return 0
            # Recursively find the sum of left and right subtrees
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            # Calculate the sum of the current subtree
            subtree_sum = node.val + left_sum + right_sum
            # Increment the counter for the subtree sum
            subtree_sum_counter[subtree_sum] += 1
            return subtree_sum

        # Initialize a Counter to keep track of the frequency of each subtree sum
        subtree_sum_counter = Counter()
        # Start the DFS traversal from the root to fill the subtree_sum_counter
        dfs(root)
        # Find the maximum frequency among the subtree sums
        max_frequency = max(subtree_sum_counter.values())
        # Collect all subtree sums with the maximum frequency
        return [subtree_sum for subtree_sum, frequency in subtree_sum_counter.items() if frequency == max_frequency]