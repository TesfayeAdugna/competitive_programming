class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    
        def helper(idx1, idx2):
            neighbours = []
            if idx1-1 >= 0:
                neighbours.append((idx1-1, idx2))
            if idx1 + 1 < m:
                neighbours.append((idx1+1, idx2))
            if idx2 + 1 < n:
                neighbours.append((idx1, idx2+1))
            if idx2 - 1 >= 0:
                neighbours.append((idx1, idx2-1))
            return neighbours
            
        # bfs algorithm
        level = 0
        while queue:
            flag = False
            for _ in range(len(queue)):
                orange = queue.popleft()
                orange_neighbours = helper(orange[0], orange[1])
                for indexs in orange_neighbours:
                    if grid[indexs[0]][indexs[1]] == 1:
                        queue.append((indexs[0], indexs[1]))
                        grid[indexs[0]][indexs[1]] = 2  
                        flag = True
            if flag:
                level += 1
                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return level
                
                
                
                
                
                
                