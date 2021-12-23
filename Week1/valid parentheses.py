class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)<=1 or len(s)%2 !=0:
            return False
        else:
            dictionary = {'(':')','{':'}','[':']'}
            opening=['(','{','[']
            closing=[')','}',']']

            output = []

            for i in s:
                if i in opening:
                    output.append(i)
                elif len(output)==0:
                    return False
                elif i in closing and dictionary[output[-1]] == i:
                    output.pop()
                else:
                    return False

            if len(output) == 0:
                return True
            else:
                return False
