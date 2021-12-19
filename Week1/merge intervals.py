class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """       
        
        intervals = sorted(intervals)
        
        if len(intervals)>1:
            mergedlist = []
            mergedlist.append(intervals[0])
            for i in range(1,len(intervals)):
                if mergedlist[-1][1] < intervals[i][0]:
                    mergedlist.append(intervals[i])
                else:      
                    mergedlist[-1][1]=max(intervals[i][1],mergedlist[-1][1])
            return mergedlist
        else:
            return intervals