class Solution:
    def longestStrChain(self, words: List[str]) -> int:


        len_map = defaultdict(set)
        for word in words:
            len_map[len(word)].add(word)
        len_map = sorted(len_map.items())
        
        N = len(len_map)
        adj = defaultdict(list)
        for i in range(1, N):
            (p, prev), (c, cur) = len_map[i - 1], len_map[i]
            if c - p != 1:
                continue
            for word in cur:
                for i in range(c):
                    temp = word[:i] + word[i + 1:]
                    if temp in prev:
                        adj[word].append(temp)
        # print(adj)
        
        @lru_cache(maxsize=None)
        def dfs(word: str) -> int:
            return 1 + max((dfs(neigh) for neigh in adj[word]), default=0)
                
        
        res = 0
        for length, words in len_map:
            res = max(res, max(dfs(word) for word in words))
        return res
