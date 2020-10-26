class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:

        n, s, cache = len(A), sum(A), {}

        for k in range(1, n // 2 + 1):
            if s * k % n == 0 and self.dfs(A, s * k // n, k, 0, cache):
                return True
        return False

    def dfs(self, A, target, k, i, cache):
        if k < 0 or k > len(A) - i:
            return False
        if k == 0 or i == len(A):
            return target == 0
        if (target, k, i) in cache:
            return cache[(target, k, i)]

        cache[(target, k, i)] = self.dfs(A, target - A[i], k - 1, i + 1, cache) or self.dfs(A, target, k, i + 1, cache)

        return cache[(target, k, i)]