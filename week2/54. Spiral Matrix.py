class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0 or len(matrix[0])==0:return []
        nums=[];m=0;n=0;row=len(matrix)-1;col=len(matrix[0])-1;flag=0;
        for n in range(col+1):nums.append(matrix[m][n])
        while row>=0 and col>=0:
            if flag % 4 == 0:
                for i in range(row):
                    m+=1
                    nums.append(matrix[m][n])
                row -= 1
            elif flag % 4==1:
                for i in range(col):
                    n-=1
                    nums.append(matrix[m][n])
                col -= 1
            elif flag % 4 == 2:
                for i in range(row):
                    m-=1
                    nums.append(matrix[m][n])
                row -= 1
            elif flag % 4 == 3:
                for i in range(col):
                    n+=1
                    nums.append(matrix[m][n])
                col -= 1
            flag+=1
        return nums