class Solution:

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.memo = {}
        return self.helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)

    def helper(self, nums, desiredTotal):
        s = str(nums)
        if s in self.memo:
            return self.memo[s]

        if nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums)):
            if not self.helper(list(nums[:i]) + list(nums[i + 1:]), desiredTotal - nums[i]):
                self.memo[s] = True
                return True

        self.memo[s] = False
        return False