"""
You are given a list of integers nums, representing the number of chess matches each person has won. Return a relative ranking (0-indexed) of each person. If two players have won the same amount, their ranking should be the same.
"""

class Solution:
    def solve(self, nums):
        nums_sorted = reversed(sorted(set(nums)))
        # print(nums_sorted)
        position = 0
        mp = {}
        for i in nums_sorted:
            mp[i] = position
            position += 1
        leaderboard = []     
        for i in nums:
            leaderboard.append(mp[i])

        return leaderboard