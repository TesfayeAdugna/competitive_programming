class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        self.ans = []
        def dfs(path):
            flag = False
            opening, closing = 0, 0
            for bracket in path:
                if bracket == "(":
                    opening += 1
                if bracket == ")":
                    closing += 1
            if opening == closing:
                flag = True

            if len(path) == 2*n and flag:
                self.ans.append(path)
                return
            if len(path) == 2*n:
                return

            dfs(path+"(")
            if not flag:
                dfs(path+")")

            return

        dfs("")
        return self.ans
