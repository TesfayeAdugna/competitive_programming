class Solution:
    def largestNumber(self, nums: List[int]) -> str:
                
        numstr = [str(x) for x in nums]
        numstrsort = sorted(numstr)
        new = []
        for j in range(len(numstrsort)):
            new.append(numstrsort[-1-j])
            
            
        length = len(new)
        for i in range(14):    
            for i in range(length):
                if new[i] !='0':
                    break
                elif i == len(new)-1 and new[i] == '0':
                    return '0'

            for i in range(len(new)-1):
                x = new[i]
                y = new[i+1]

                xy = x + y
                yx = y + x
                xyi = int(xy)
                yxi = int(yx)

                if xyi >= yxi:
                    continue
                else:
                    temp = new[i]
                    new[i] = new[i+1]
                    new[i+1] = temp

        final = "".join(str(item) for item in new)
        return final