# array & hashing
# https://leetcode.com/problems/group-anagrams/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return strs

        anagram_groups = {}
        for str in strs:
            key = "".join(sorted(str))
            print(key)
            if anagram_groups.get(key):
                anagram_groups[key].append(str)
            else:
                anagram_groups[key] = [str]

        return list(anagram_groups.values())


# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

sol = Solution()

print(sol.groupAnagrams(strs))
