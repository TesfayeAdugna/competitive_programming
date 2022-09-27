class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        
                
        
        dic = {}
        for i in range(len(graph)):
            dic[i] = graph[i]
        
        self.ans = []
        
        def dfs(idx, path):
            if idx == len(graph) - 1:
                self.ans.append(path)
                return self.ans
            
            for i in dic[idx]:
                dfs(i, path + [i])
            return self.ans
        
        return dfs(0, [0])