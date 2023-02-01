class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:



        team, Result = [], 0
        for i in range(len(ages)):
            team.append((ages[i], scores[i]))

        team.sort()
        
        Cache = [0 for _ in range(len(ages))]
        for i in range(len(ages)):
            Cache[i] = team[i][1]
            for j in range(i):
                if team[i][1] >= team[j][1]:
                    Cache[i] = max(Cache[i], Cache[j] + team[i][1])
            Result = max(Result, Cache[i])
        
        return Result
