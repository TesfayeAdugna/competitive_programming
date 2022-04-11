"""
https://leetcode.com/problems/course-schedule/
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        dic = {}
        for ele in prerequisites:
            if ele[0] not in dic:
                dic[ele[0]] = 1
            else:
                dic[ele[0]] +=1
            if ele[1] not in dic:
                dic[ele[1]] = 0
                
        print(dic)
        queue = deque()
        visited = []
        for ele in dic:
            if dic[ele] == 0:
                queue.append(ele)
                
        while queue:
            curr = queue.popleft()
            visited.append(curr)
            
            for i in range(len(prerequisites)):
                if curr == prerequisites[i][1]:
                    dic[prerequisites[i][0]]-=1
                    if dic[prerequisites[i][0]] == 0:
                        queue.append(prerequisites[i][0])
                        
        return len(visited) == len(dic)
    
    
    