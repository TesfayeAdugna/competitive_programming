"""
https://leetcode.com/problems/course-schedule-ii/
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = {}
        for ele in prerequisites:
            if ele[0] not in dic:
                dic[ele[0]] = 1
            else:
                dic[ele[0]] +=1
            if ele[1] not in dic:
                dic[ele[1]] = 0
                
        for j in range(numCourses):
            if j not in dic:
                dic[j] = 0                
                
        queue = deque()
        for ele in dic:
            if dic[ele] == 0:
                queue.append(ele)
                
        visited = []
        while queue:
            curr = queue.popleft()
            visited.append(curr)
            for i in range(len(prerequisites)):
                if curr == prerequisites[i][1]:
                    dic[prerequisites[i][0]]-=1
                    if dic[prerequisites[i][0]] == 0:
                        queue.append(prerequisites[i][0])
                    
        return visited if len(visited) == len(dic) else []