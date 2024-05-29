"""
Given a number represented by a list of digits, find the next greater permutation of a number, 
in terms of lexicographic ordering. If there is not greater permutation possible, 
return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. 
The list [1,3,2] should return [2,1,3]. 
The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
"""

from typing import List

# Solution
class Solution:
    def nextPermutation(self, nums: List[int])-> None:
        pivotIndex = None

        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i - 1]:
                pivotIndex = i - 1
                break
        else:
            nums.reverse()
            return
        
        swapIndex = len(nums) - 1

        while nums(swapIndex) <= nums[pivotIndex]:
            swapIndex -= 1

        nums[pivotIndex], nums[swapIndex] = nums[swapIndex],nums[pivotIndex]
        nums[pivotIndex + 1:] = reversed(nums[pivotIndex + 1:])

        return


#test solution
def test_solution():
    sol = Solution()
    test_array = [4,3,2,1]
    sol.nextPermutation(test_array)
    assert test_array == [1, 2, 3, 4]

test_solution()