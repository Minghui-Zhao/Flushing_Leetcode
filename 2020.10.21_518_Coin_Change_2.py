# 518. Coin Change 2

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for j in range(amount + 1)] for i in range(2)]
        dp[0][0] = 1

        for i in range(1, len(coins) + 1):
            dp[i % 2][0] = 1

            for j in range(1, amount + 1):
                curNum = coins[i - 1]
                dp[i % 2][j] = dp[(i - 1) % 2][j]

                if curNum <= j:
                    dp[i % 2][j] += dp[i % 2][j - curNum]

        return dp[len(coins) % 2][-1]