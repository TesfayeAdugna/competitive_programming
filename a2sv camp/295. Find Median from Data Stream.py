"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
"""

class MedianFinder(object):

    def __init__(self):
        maxheap = []
        minheap = []
        self.maxheap = maxheap
        self.minheap = minheap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.maxheap,-1*num)
        
        if len(self.maxheap) - len(self.minheap) == 2:
            heapq.heappush(self.minheap, -1*heapq.heappop(self.maxheap))
        if len(self.minheap)>0 and -1*self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.minheap,-1*heapq.heappop(self.maxheap))
            heapq.heappush(self.maxheap,-1*heapq.heappop(self.minheap))

    def findMedian(self):
        """
        :rtype: float
        """
        len1 = len(self.maxheap)
        len2 = len(self.minheap)
        
        if len1>len2:
            return (-1*self.maxheap[0]) * 1.0
        
        if len1==len2:
            return (-1*self.maxheap[0] + self.minheap[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()