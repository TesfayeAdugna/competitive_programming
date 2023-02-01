class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        result, grid = [], []
        for i in range(len(mat)+1):
            temp1 = [0 for _ in range(len(mat[0])+1)]
            grid.append(temp1)
            if i != len(mat):
                temp2 = [0]*len(mat[0])
                result.append(temp2)

        if len(mat)>1: grid[1][1] = mat[0][0]
        if len(mat[0])>1: grid[1][2] = mat[0][1]

        for i in range(1,len(mat)): grid[i+1][1] = grid[i][1] + mat[i][0]

        for i in range(1,len(mat[0])): grid[1][i+1] = grid[1][i] + mat[0][i]

        for i in range(1,len(mat)):
            for j in range(1,len(mat[0])):
                grid[i+1][j+1] = grid[i][j+1] + grid[i+1][j] - grid[i][j] + mat[i][j]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                maximum_x = min(i+k,len(mat)-1)
                maximum_y = min(j+k,len(mat[0])-1)
                minimum_x = max(i-k,0)
                minimum_y = max(j-k,0)
                result[i][j] = grid[maximum_x +1][maximum_y +1] - grid[minimum_x ][maximum_y +1] - grid[maximum_x +1][minimum_y ] + grid[minimum_x ][minimum_y]
                
        return result



