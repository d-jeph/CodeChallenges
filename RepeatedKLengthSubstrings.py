"""
Given a string s and an integer k, return the number of k-length substrings that occur more than once in s.
"""
class Solution:
    def solve(self, s, k):
        seen = []
        mp = {}
        for i in range(len(s) - k + 1):
            substring = s[i : i + k]
            if mp.get(substring) is None:
                mp[substring] = 1
            else:
                mp[substring] += 1
        return sum(1 for x in mp.values() if x > 1)