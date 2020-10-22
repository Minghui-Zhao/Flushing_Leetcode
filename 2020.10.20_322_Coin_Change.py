# 322. Coin Change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return -1
        if amount == 0:
            return 0

        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return dp[-1] if dp[-1] != inf else -1
