class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:



        memo = defaultdict(set)
        
        for id, time in logs:
            memo[id].add(time)
        
        result = [0] * k
        
        for user in memo:
            result[len(memo[user]) - 1] += 1
        
        return result
