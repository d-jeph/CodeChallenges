from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_elements = Counter(nums)

        frequent_elements = {
            k: v
            for k, v in sorted(
                frequent_elements.items(), key=lambda item: item[1], reverse=True
            )
        }

        print(frequent_elements)
        result = list(frequent_elements.keys())[:k]

        return result


sol = Solution()

print(sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
