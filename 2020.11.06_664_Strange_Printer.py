class Solution:

    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for d in range(1, len(s)):
            for l in range(0, len(s) - d):
                r = l + d
                dp[l][r] = 1 + dp[l + 1][r]
                for i in range(l + 1, r + 1):
                    if s[i] == s[l]:
                        dp[l][r] = min(dp[l][r], dp[l][i - 1] + (dp[i + 1][r] if i + 1 <= r else 0))
        return dp[0][-1]