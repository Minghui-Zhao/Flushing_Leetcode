# 486. Predict the Winner

class Solution:
    def PredictTheWinner(self, nums):
        n = len(nums)
        memo = {}
        firstSum = self.dfs(nums, 0, n - 1, memo)
        totalSum = sum(nums)
        return firstSum >= totalSum - firstSum

    def dfs(self, nums, i, j, memo):
        # Base case.
        if i > j:
            return 0
        if i == j:
            return nums[i]
        if (i, j) in memo:
            return memo[(i, j)]
        memo[(i, j)] = max(nums[i] + min(self.dfs(nums, i + 2, j, memo), self.dfs(nums, i + 1, j - 1, memo)),
                           nums[j] + min(self.dfs(nums, i, j - 2, memo), self.dfs(nums, i + 1, j - 1, memo)))
        return memo[(i, j)]
