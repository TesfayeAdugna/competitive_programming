class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        adjacency = {}

        for p in adjacentPairs:
            if p[0] not in adjacency:
                adjacency[p[0]] = set()
            adjacency[p[0]].add(p[1])

            if p[1] not in adjacency:
                adjacency[p[1]] = set()
            adjacency[p[1]].add(p[0])

        l = len(adjacency)
        res = [float(inf)]*l
        s = set()

        for k in adjacency:
            if len(adjacency[k])==1:
                if res[0]==float(inf):
                    res[0] = k
                else:
                    res[l-1] = k
            if res[0]!=float(inf) and res[l-1]!=float(inf):
                break

        for i in range(0, l-1):
            element = list(adjacency[res[i]])[0]
            res[i+1] = element
            adjacency[element].remove(res[i])
        return res
