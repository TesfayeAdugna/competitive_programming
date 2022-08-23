class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build the graph using dictionary.
        visited = [0] * numCourses
        graph = defaultdict(list)
        for courses in prerequisites:
            graph[courses[1]].append(courses[0])
            visited[courses[0]] += 1
            
        # find a node with no incoming edge and add it to queue.
        queue = deque()
        for i in range(numCourses):
            if visited[i] == 0:
                queue.append(i)
                
        # topological sort algorithm - bfs approach.
        total_courses = 0
        while queue:
            course = queue.popleft()
            total_courses += 1
            for prerequisite in graph[course]:
                visited[prerequisite] -= 1
                if visited[prerequisite] == 0:
                    queue.append(prerequisite)
                    
        return total_courses == numCourses