"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        
        def dfs(index1,index2):
            if index1<0 or index2<0 or index1 == m or index2 == n or board[index1][index2] != "O":
                return
            board[index1][index2] = "T"
            dfs(index1,index2+1)
            dfs(index1,index2-1)
            dfs(index1+1,index2)
            dfs(index1-1,index2)
        
        m=len(board)
        n=len(board[0])
        
        #capture unsorrounded regions
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1:
                    if board[i][j]== "O":
                        dfs(i,j)
                        
                if j == 0 or j == n-1:
                    if board[i][j] == "O":
                        dfs(i,j)
        
        #change surrounded "O"s to "X"
        for k in range(m):
            for l in range(n):
                if board[k][l] == "O":
                    board[k][l] = "X"
                    
        #change unsurrounded "O" back to O
        for o in range(m):
            for p in range(n):
                if board[o][p] == "T":
                    board[o][p] = "O"
        
        
        
        
        