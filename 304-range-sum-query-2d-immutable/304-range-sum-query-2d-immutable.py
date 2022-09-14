class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.prefix = []
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix[0])):
                if not temp:
                    temp.append(matrix[i][j])
                else:
                    temp.append(temp[-1]+matrix[i][j])
            self.prefix.append(temp)
        
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ = 0
        for i in range(row1, row2+1):
            if col1 > 0:
                summ += self.prefix[i][col2] - self.prefix[i][col1-1]
            else:
                summ += self.prefix[i][col2]
                
        return summ


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)