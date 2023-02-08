class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:


        adj = defaultdict(lambda :defaultdict(lambda :-1))
        for (a, b), v in zip(equations, values):
            adj[a][b] = v
            adj[b][a] = 1.0 / v
        
        for start in adj:
            bfs = deque([(start, 1)])
            been = set()
            while bfs:
                node, v = bfs.popleft()
                for next in adj[node]:
                    if next in been:
                        continue
                    been.add(next)
                    adj[start][next] = v * adj[node][next]
                    bfs.append((next, adj[start][next]))
        
        return [adj[a][b] for a, b in queries]
