class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        d = {}
        g = defaultdict(set)
        for act in accounts:
            name = act[0]
            if act[1:]:
                for email in act[1:]:
                    g[act[1]].add(email)
                    g[email].add(act[1])
                    d[email] = name
                    
        seen = set()
        stack = []
        res = []
        for email in g:
            if email not in seen:
                stack.append(email)
                lst = []
                while stack:
                    curr = stack.pop()
                    seen.add(curr)
                    lst.append(curr)
                    for ne in g[curr]:
                        if ne not in seen:
                            seen.add(ne)
                            stack.append(ne)
                res.append([d.get(email)]+sorted(lst))
        return res