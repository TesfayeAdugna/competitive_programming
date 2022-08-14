class Solution:
    def findLadders(self,  beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        neighbors = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = f"{word[:j]}*{word[j+1:]}"
                neighbors[pattern].append(word)

        def bfs() -> int:
            visited = set([beginWord])
            queue = deque([beginWord])
            depth = 1
            while queue:
                for _ in range(len(queue)):
                    word = queue.popleft()
                    if word == endWord:
                        return depth
                    for j in range(len(word)):
                        pattern = f"{word[:j]}*{word[j+1:]}"
                        for neighbor in neighbors[pattern]:
                            if neighbor in visited:
                                continue
                            visited.add(neighbor)
                            queue.append(neighbor)
                depth += 1

        @lru_cache(maxsize=None)
        def dfs_backtrack(word, depth):
            if word == endWord:
                return [[word]]
            elif depth == 1:
                return
            else:
                results = []
                visited.add(word)
                for i in range(len(word)):
                    pattern = f"{word[:i]}*{word[i+1:]}"
                    for neighbor in neighbors[pattern]:
                        if neighbor in visited:
                            continue
                        result = dfs_backtrack(neighbor, depth - 1)
                        if result:
                            for r in result:
                                results.append([word] + r)
                visited.remove(word)
                return results

        depth = bfs()
        visited = set([beginWord])
        results = []

        results = dfs_backtrack(beginWord, depth)

        return results