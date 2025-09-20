class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(mat), len(mat[0])
        result = []
        d = m + n -2
        for d in range(d+1):
            diagonal = []
            for row in range(max(0, d - n + 1), min(m, d + 1)):
                col = d -row
                diagonal.append(mat[row][col])
            if d % 2 == 0:
                diagonal.reverse()
            result.extend(diagonal)
        return result

        