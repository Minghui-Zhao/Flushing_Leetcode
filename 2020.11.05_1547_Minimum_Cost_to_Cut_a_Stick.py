
class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        f = [None] * len(cuts)
        for i in range(len(f)):
            f[i] = [None] * len(cuts)

        for l in range(1, len(cuts) + 1):
            for i in range(len(cuts) - l + 1):
                j = i + l - 1
                if i + 1 >= j:
                    f[i][j] = 0
                    continue

                min_cost = float('inf')
                for k in range(i + 1, j):
                    cost = f[i][k] + f[k][j] + cuts[j] - cuts[i]
                    min_cost = min(min_cost, cost)
                f[i][j] = min_cost

        return f[0][len(cuts) - 1]
