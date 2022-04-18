"""
https://leetcode.com/problems/number-of-provinces/
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        self.num = len(isConnected)
          
        def Union(idx1, idx2):
            x = find(idx1)
            y = find(idx2)
            if x != y:
                if rank[x]>=rank[y]:
                    parent[y] = x
                    rank[y] -= 1
                    rank[x] += 1
                else:
                    parent[x] = y
                    rank[x] -= 1
                    rank[y] += 1
                self.num-=1
                    
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
            
        n = len(isConnected)
        parent = [x for x in range(n)]
        rank = [1]*n
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    Union(i,j)
            
        return self.num
                    