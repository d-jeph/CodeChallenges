"""
Given a binary tree root, return whether it's a binary search tree. A binary tree node is a binary search tree if :

All nodes on its left subtree are smaller than node.val
All nodes on its right subtree are bigger than node.val
All nodes hold the these properties.
"""


# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root is None:
            return True

        return self.is_bst(root, float('-inf'), float('inf'))



    def is_bst(self,node, min, max):
        if node.val <= min:
            return False

        if node.val >= max:
            return False

        left_child_check = True
        right_child_check = True

        if node.left is not None:
            left_child_check = self.is_bst(node.left, min, node.val)
        if node.right is not None:
            right_child_check = self.is_bst(node.right, node.val, max)

        return left_child_check and right_child_check
        