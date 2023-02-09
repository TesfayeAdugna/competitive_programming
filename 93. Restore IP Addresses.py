class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        result = []
        self.backtrack(s, 0, [], result)
        return result

    def isValid(self, s: str) -> bool:
        if len(s) > 1 and s[0] == '0':
            return False
        return 0 <= int(s) <= 255
        
    def backtrack(self, s, start, segments, res):
        if start == len(s) and len(segments) == 4:
            res.append('.'.join(segments))
            return
        if len(segments) >= 4:
            return
        for end in range(start, min(start+3, len(s))):
            segment = s[start:end+1]
            if self.isValid(segment):
                self.backtrack(s, end+1, segments + [segment], res)
