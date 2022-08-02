class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []
        for i in range(len(heights)):
            temp = [i, heights[i]]
            if not stack:
                stack.append(temp)
            else:
                x = None
                while stack and stack[-1][1] > temp[1]:
                    area = stack[-1][1] * (temp[0] - stack[-1][0])
                    maxArea = max(maxArea, area)
                    x = stack.pop()
                if x:
                    if temp[0] == len(heights)-1:
                        area = temp[1] * (temp[0] - x[0] + 1)
                        maxArea = max(maxArea, area)
                    else:
                        temp[0] = x[0]
                stack.append(temp)
                
        for i in range(len(stack)):
            area = stack[i][1] * (stack[-1][0] - stack[i][0] + 1)
            maxArea = max(area, maxArea)

        return maxArea
    