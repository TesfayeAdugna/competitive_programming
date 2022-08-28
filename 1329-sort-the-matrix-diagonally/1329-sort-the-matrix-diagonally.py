class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        # collect the diagonals into a dictionary
        for i in range(m):
            for j in range(n):
                diagonals[i - j].append(mat[i][j])
        # reverse sort the diagonals list.
        for k in diagonals:
            diagonals[k].sort(reverse=True)
        # put the values back into the matrix.
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()
        return mat