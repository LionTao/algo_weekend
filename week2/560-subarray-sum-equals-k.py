"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。
"""
from typing import List
import collections
class Solution:
    """
    计算前缀和与利用dict作为哈希表查询
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum_map = collections.defaultdict(int) # 默认每个都是0
        presum_map[0] = 1
        presum, ans = 0, 0

        for i in range(len(nums)):
            presum += nums[i]
            target = presum - k
            if target in presum_map:
                ans += presum_map[target]
            presum_map[presum] += 1
        
        return ans