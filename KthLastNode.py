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
        if length >= k:
            curr = node
            for i in range(length - k-1):
                curr = curr.next
            
        return curr.val