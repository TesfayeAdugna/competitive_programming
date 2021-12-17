class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = list(s.split())
        emptystr = []
        for i in range(len(li)):
            for j in li:
                if j[-1] == str(i+1):
                    emptystr.append(j[:-1])
        return " ".join(map(str,emptystr))