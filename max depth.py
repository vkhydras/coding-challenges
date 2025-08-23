# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def traverse(node):
            if node is None:
                return 0
            left_d = traverse(node.left)
            right_d = traverse(node.right)
            return 1 + max(left_d,right_d)
        return traverse(root)        
        