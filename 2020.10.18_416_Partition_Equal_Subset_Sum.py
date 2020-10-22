# 416. Partition Equal Subset Sum

class Solution:
    def canPartition(self, nums) -> bool:
        if not nums or len(nums) < 2:
            return False
        sumVal = sum(nums)
        if sumVal % 2 != 0:
            return False

        cache = [[-1 for j in range(sumVal // 2 + 1)] for i in range(len(nums) + 1)]

        return self.helper(nums, len(nums) - 1, sumVal // 2, cache)

    def helper(self, nums, i, target, cache):
        if target == 0:
            return True
        if target < 0 or i < 0:
            return False

        if cache[i][target] != -1:
            return cache[i][target]

        if nums[i] <= target:
            cache[i][target] = self.helper(nums, i - 1, target - nums[i], cache) or self.helper(nums, i - 1, target,
                                                                                                cache)
            return cache[i][target]
