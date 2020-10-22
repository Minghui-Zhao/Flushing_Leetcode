# 494. Target Sum

from collections import defaultdict


# Solution 1: DFS with cache - O(n^2)

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        cache = defaultdict(dict)
        return self.dfs(nums, S, 0, 0, cache)

    def dfs(self, nums, target, i, curSum, cache):
        if i == len(nums):
            return 1 if curSum == target else 0

        if i in cache and curSum in cache[i]:
            return cache[i][curSum]

        cache[i][curSum] = self.dfs(nums, target, i + 1, curSum + nums[i], cache) + self.dfs(nums, target, i + 1,
                                                                                             curSum - nums[i], cache)
        return cache[i][curSum]


# Solution 2: DFS Bruteforce - O(2^n)

class Solution:
    res = 0
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        res = []
        if not nums:
            return res

        self.dfs(nums, S, 0, 0, res)
        return sum(res)

    def dfs(self, nums, target, i, curSum, res):

        if i == len(nums):
            if curSum == target:
                res.append(1)
            return

        self.dfs(nums, target, i+1, curSum+nums[i], res)

        self.dfs(nums, target, i+1, curSum-nums[i], res)
