class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickers.sort(key=lambda x: len(x), reverse=True)
        temp = []
        for s in stickers:
            temp1 = {}
            for i in s:
                temp1[i] = temp1.get(i, 0) + 1
            temp.append(temp1)
        stickers = temp
        memo = {'': 0}

        def dfs(target):
            if target in memo:
                return memo[target]
            res = float('inf')
            for stick in stickers:
                if target[0] not in stick:
                    continue
                targetnew = target
                for s in stick:
                    targetnew = targetnew.replace(s, '', stick[s])
                if targetnew == '':
                    res = 1
                    break
                elif targetnew != target:
                    res = min(res, 1 + dfs(targetnew))
            memo[target] = res
            return res

        res = dfs(target)
        if res == float('inf'):
            return -1
        return res