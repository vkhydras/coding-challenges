class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_sum = 0
        m, n = len(grid), len(grid[0])
        for i in range(1,m-1):
            for j in range(1,n-1):
                top_row = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                bottom_row = grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                sum = top_row + grid[i][j] + bottom_row
                max_sum = max(sum,max_sum)
        return max_sum
        