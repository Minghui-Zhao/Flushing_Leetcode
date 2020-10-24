# 1049. Last Stone Weight II

# Solution 1: dfs with cache
import collections


class Solution:
    def lastStoneWeightII(self, stones) -> int:
        cache = collections.defaultdict(dict)
        return self.dfs(0, 0, stones, cache)

    def dfs(self, sum1, sum2, stones, cache):
        if len(stones) == 0:
            return abs(sum1 - sum2)

        if sum1 in cache and sum2 in cache[sum1]:
            return cache[sum1][sum2]

        e = stones.pop()
        cache[sum1][sum2] = min(self.dfs(sum1 + e, sum2, stones, cache), self.dfs(sum1, sum2 + e, stones, cache))
        stones.append(e)

        return cache[sum1][sum2]