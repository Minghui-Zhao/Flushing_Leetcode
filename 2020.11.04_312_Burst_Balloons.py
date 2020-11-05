class Solution:

    def maxCoins(self, nums: list) -> int:
        n = len(nums) + 2
        new_nums = [1] * n

        for i in range(n - 2):
            new_nums[i + 1] = nums[i]

        dp = [[0] * n for i in range(n)]

        return self.burst(new_nums, dp, 1, n - 2)

    def burst(self, nums, dp, i, j):
        if i > j:
            return 0

        if dp[i][j] != 0:
            return dp[i][j]

        res = 0
        for k in range(i, j + 1):
            res = max(res, nums[i - 1] * nums[k] * nums[j + 1] +
                      self.burst(nums, dp, i, k - 1) +
                      self.burst(nums, dp, k + 1, j))

        dp[i][j] = res

        return res