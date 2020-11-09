# Solution 1: DP
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[(0, 0)] * n for _ in range(n)] # (max_val, min_cost)
        for size in range(n):
            for i in range(n - size):
                # [i, i+size]
                if size == 0:
                    dp[i][i + size] = (arr[i], 0)
                    continue
                max_val, min_cost = 0, float('inf')
                for j in range(i, i + size):
                    max_val = max(dp[i][j][0], dp[j + 1][i + size][0])
                    min_cost = min(min_cost,
                                   dp[i][j][1] + dp[j + 1][i + size][1] + dp[i][j][0] * dp[j + 1][i + size][0])
                dp[i][i + size] = (max_val, min_cost)
        return dp[0][n - 1][1]

# Solution 2: stack
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res