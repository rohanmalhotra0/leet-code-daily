from collections import defaultdict
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        cur_sum = 0
        left = 0

        for right in range(len(nums)):
            # include nums[right]
            cur_sum += nums[right]
            count[nums[right]] += 1

            # if window grows too big, pop from left
            if right - left + 1 > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                cur_sum -= nums[left]
                left += 1

            # if window is size k and all k are distinct
            if right - left + 1 == k and len(count) == k:
                res = max(res, cur_sum)

        return res
