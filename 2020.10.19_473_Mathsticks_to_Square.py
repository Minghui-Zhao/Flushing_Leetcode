# 473. Matchsticks to Square

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 4:
            return False
        sumVal = sum(nums)
        if sumVal % 4 != 0:
            return False

        targetArr = [0] * 4
        nums = sorted(nums)[::-1]  # sort to accelerate the dfs searching process

        return self.dfs(nums, targetArr, 0, sumVal // 4)

    def dfs(self, nums, targetArr, idx, target):
        if idx >= len(nums):
            if targetArr[0] == target and targetArr[1] == target and targetArr[2] == target:
                return True
            return False

        for i in range(4):
            if targetArr[i] + nums[idx] > target:
                continue

            targetArr[i] += nums[idx]
            if self.dfs(nums, targetArr, idx + 1, target):
                return True
            targetArr[i] -= nums[idx]

        return False

