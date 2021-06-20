"""
Given a singly linked list node, return the value of the kth last node (0-indexed). k is guaranteed not to be larger than the size of the linked list.

This should be done in \mathcal{O}(1)O(1) space.
"""
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        length = 0
        curr = node
    
        # count the total number of nodes in the linked list
        while curr:
            curr = curr.next
            length = length + 1
    
        # if k is not more than list size
        if k <= length:
            curr = node
            for i in range(length - k-1):
                curr = curr.next
            
        return curr.val