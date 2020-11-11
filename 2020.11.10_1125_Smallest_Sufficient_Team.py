class Solution:
    def smallestSufficientTeam(self, S: List[str], P: List[List[str]]) -> List[int]:
        s = set(S)
        res = [[]]

        for i in range(len(P)):
            P[i] = set(P[i])

        for i, i_skills in enumerate(P):
            for j, j_skills in enumerate(P):
                if i != j and i_skills.issubset(j_skills):
                    P[i] = set()

        people = sorted(filter(lambda x: x[1], list(enumerate(P))), key=lambda x: len(x[1]), reverse=True)

        def helper(s, p, i, res):
            if res[0] and len(p) > len(res[0]):
                return

            if not s:
                if not res[0] or len(p) < len(res[0]):
                    res[0] = list(p)
                    return

            if i >= len(people):
                return

            skills_left = s - set(people[i][1])
            p.append(people[i][0])
            helper(skills_left, p, i + 1, res)
            p.pop()

            helper(s, p, i + 1, res)

        helper(s, [], 0, res)
        return sorted(res[0])