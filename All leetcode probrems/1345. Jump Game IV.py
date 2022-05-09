"""
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Constraints:

1 <= arr.length <= 5 * 104
-108 <= arr[i] <= 108
"""
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        last = len(arr)-1
        
        dictOfIndexs = {}
        
        for i in range(len(arr)):
            if arr[i] in dictOfIndexs:
                dictOfIndexs[arr[i]].append(i)
            else:
                dictOfIndexs[arr[i]] = [i]
                
        def bfs(start):
            queue = collections.deque([start])
            visited = set()
            
            visited.add(start)
            
            result = 0
            
            while queue:
                n = len(queue)
                
                for j in range(n):
                    current = queue.popleft()
                    if current == last:
                        return result
                    else:
                        if current>0 and current-1 not in visited:
                            queue.append(current-1)
                            visited.add(current-1)
                        if current<last and current+1 not in visited:
                            queue.append(current+1)
                            visited.add(current+1)
                        for i in dictOfIndexs[arr[current]]:
                            if i not in visited:
                                queue.append(i)
                                visited.add(i)
                        dictOfIndexs[arr[current]] = []
                result += 1
            
        return bfs(0)
            
            