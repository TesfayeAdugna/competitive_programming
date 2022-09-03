class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        s=[str(i)for i in range(1,10)]
        while len(s[0])!=n:
            l=[]
            for i in s:
                o=int(i[-1])
                if o-k>=0:
                    l+=[i+str(o-k)]
                if o+k<10:
                    l+=[i+str(o+k)]
            s=list(set(l))
        return list(set(s))