"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n
"""

class Solution(object):
    
    
    def seeneighbor(self, image,sr,sc,newColor,temp,stack,tuples):
        sr = stack[0][0]
        sc = stack[0][1]
        if (sr,sc) not in tuples:
            if sr>0 and temp == image[sr-1][sc]:
                stack.append([sr-1,sc])

            if sr < len(image)-1 and temp == image[sr+1][sc]:
                stack.append([sr+1,sc])

            if sc > 0 and temp == image[sr][sc-1]:
                stack.append([sr,sc-1])

            if sc < len(image[sr])-1 and temp == image[sr][sc+1]:
                stack.append([sr,sc+1])

            image[sr][sc] = newColor
            tuples.add((sr,sc))
            
        stack.pop(0)
        
        if len(stack)<1:
            return image
        else:
            return self.seeneighbor(image,sr,sc,newColor,temp,stack,tuples)
    
    
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        temp = image[sr][sc]
                
        stack = []
        tuples = set()
        stack.append([sr,sc])
        
        
            
        return self.seeneighbor(image,sr,sc,newColor,temp,stack,tuples)
        
        
        
        
        