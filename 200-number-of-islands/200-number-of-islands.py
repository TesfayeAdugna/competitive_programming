class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        n, m = len(grid), len(grid[0])
        
        def findneighbours(i, j):
            neighbours = []
            if i > 0 and grid[i-1][j] == "1":
                neighbours.append((i-1, j))
            if i < n-1 and grid[i+1][j] == "1":
                neighbours.append((i+1, j))
            if j > 0 and grid[i][j-1] == "1":
                neighbours.append((i, j-1))
            if j < m-1 and grid[i][j+1] == "1":
                neighbours.append((i, j+1))
            return neighbours
            
        visited = set()
        
        def bfs(i, j):
            visited.add((i,j))
            queue = deque([(i, j)])
            while queue:
                for i in range(len(queue)):
                    current = queue.pop()
                    neighbours = findneighbours(current[0], current[1])
                    for neigh in neighbours:
                        if (neigh[0], neigh[1]) not in visited:
                            visited.add((neigh[0], neigh[1]))
                            queue.append((neigh[0], neigh[1]))
                        
        Answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    Answer += 1
                    bfs(i, j)
                    
        return Answer