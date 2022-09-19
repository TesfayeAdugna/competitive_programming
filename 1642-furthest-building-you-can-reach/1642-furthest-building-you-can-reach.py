class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minheap = []
        l = ladders
        best = 0
        for i in range(len(heights)-1):
            if l>0:
                if heights[i]<heights[i+1]:
                    heapq.heappush(minheap,heights[i+1]-heights[i])
                    l-=1
                    best = i+1
                elif i == len(heights)-2:
                    best = i+1
                    return best
            else:
                if heights[i]<heights[i+1]:
                    minimum = heights[i+1]-heights[i]
                    if len(minheap)>0 and minheap[0]<minimum:
                        minimum = minheap[0]

                    if bricks>= minimum:
                        bricks-=heapq.heappushpop(minheap,(heights[i+1]-heights[i]))
                        print(bricks)
                        best = i+1
                    else:
                        best = i
                        return best
                else:
                    best = i+1

        return best