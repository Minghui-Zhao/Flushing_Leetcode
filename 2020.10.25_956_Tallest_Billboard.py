# Solution 1: dfs with cache
import collections


class Solution(object):
    def tallestBillboard(self, rods):
        cache = {}
        return self.dfs(0, 0, 0, cache, rods)

    def dfs(self, i, s1, s2, cache, rods):
        if i == len(rods):
            return s1 if (s1 == s2) else -1

        if (i, abs(s1 - s2)) not in cache:
            m = max(
                self.dfs(i + 1, s1 + rods[i], s2, cache, rods),
                self.dfs(i + 1, s1, s2 + rods[i], cache, rods),
                self.dfs(i + 1, s1, s2, cache, rods))
            if m == -1:
                cache[(i, abs(s1 - s2))] = -1
            else:
                cache[(i, abs(s1 - s2))] = m - max(s1, s2)
        if cache[(i, abs(s1 - s2))] != -1:
            return max(s1, s2) + cache[(i, abs(s1 - s2))]
        else:
            return -1


# Solution 2: dp

class Solution(object):
    def tallestBillboard(self, rods):
        dp = dict()
        dp[0] = 0

        for i in rods:
            cur = collections.defaultdict(int)
            for s in dp:
                cur[s + i] = max(dp[s] + i, cur[s + i])
                cur[s] = max(dp[s], cur[s])
                cur[s - i] = max(dp[s], cur[s - i])
            dp = cur
        return dp[0]