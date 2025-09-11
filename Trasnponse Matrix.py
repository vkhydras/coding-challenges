class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        transpose = [[0] * m for k in range(n)]

        for i in range(m):
            for j in range(n):
                transpose[j][i] = matrix[i][j]

        return transpose
