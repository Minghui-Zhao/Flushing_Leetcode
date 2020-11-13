# Solution 1: DFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        n = len(M)
        visited = [0] * n

        for i in range(n):
            if visited[i] == 0:
                self.dfs(M, visited, i)
                count += 1
        return count

    def dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, visited, j)



# Solution 2: Union Find
class Solution:
    def findCircleNum(self, M):
        sets = [i for i in range(len(M))]

        def find(x):
            if x == sets[x]:
                return x
            sets[x] = find(sets[x])
            return sets[x]

        for j in range(0, len(M)):
            for i in range(j+1, len(M)):
                if M[i][j] == 1:
                    sets[find(i)] = find(j)

        return sum([1 for i, v in enumerate(sets) if i == v])
