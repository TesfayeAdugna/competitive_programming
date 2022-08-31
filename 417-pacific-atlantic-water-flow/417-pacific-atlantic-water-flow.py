class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        
        
        rows = len(heights); cols = len(heights[0]);
        # DFS to check the neighbouring cells can be visited or not
        def DFS(x: int, y: int, prevHeight: int, visited: set[tuple[int]]):
            if x<0 or x==rows or y<0 or y==cols:
                return;
            if (x,y) in visited:
                return;
            height = heights[x][y];
            if height<prevHeight:
                return;
            visited.add((x,y));
            DFS(x,y+1,height,visited);
            DFS(x,y-1,height,visited);
            DFS(x+1,y,height,visited);
            DFS(x-1,y,height,visited);
            
        pacificCoOrdinates = set();
        atlanticCoOrdinates = set();
            
        for i in range (0, rows):
            DFS(i,0,0,pacificCoOrdinates); #left column is pacific ocean seashore
            DFS(i,cols-1,0,atlanticCoOrdinates); # right column atlantic ocean seashore
        for i in range (0, cols):
            DFS(0,i,0,pacificCoOrdinates); # top row is pacific ocean seashore
            DFS(rows-1,i,0,atlanticCoOrdinates); # bottom row is atlantic ocean seashore
        
        return list(pacificCoOrdinates & atlanticCoOrdinates);
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         m, n = len(heights), len(heights[0])
        
#         def isPasific(i, j):
#             if i<0 or j<0:
#                 return True
#             return False
#         def isAtlantic(i, j):
#             if j>n-1 or i>m-1:
#                 return True
#             return False
#         def isValid(i, j):
#             if i >=0 and j>=0 and i<m and j<n:
#                 return True
#             return False
        
        
#         def dfs(i, j, Pasific, Atlantic):
#             if i > n-1 or j > n-1:
#                 Atlantic = True
#                 return
#             if i < 0 or j < 0:
#                 Pacific = True
#                 return
                
#             directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            
#             for d in directions:
#                 x, y = i+d[0], j+d[1]
#                 if isPasific(x, y):
#                     Pasific = True
#                 if isAtlantic(x, y):
#                     Atlantic = True
#                 if isPasific(x, y) or isAtlantic(x, y):
#                     return
#                 if isValid(x, y):
#                     dfs(x, y, Pasific, Atlantic)
                    
#         ans = []
#         for i in range(m):
#             for j in range(n):
#                 Pasific, Atlantic = False, False
#                 dfs(i, j, Pasific, Atlantic)
#                 if Pasific and Atlantic:
#                     ans.append([i,j])
#         return ans
                
                
                
                
                
                