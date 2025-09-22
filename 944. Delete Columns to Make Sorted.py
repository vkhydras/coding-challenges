class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        drop = 0
        for n in range(len(strs[0])): # n = column, m = row
            for m in range(1,len(strs)):
                if strs[m][n] < strs[m-1][n]:
                    drop+=1
                    break
        return drop
        
