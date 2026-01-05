# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root, leftBound, rightBound):
            if not root:
                return True
            
            if leftBound < root.val < rightBound:
                return dfs(root.left, leftBound, root.val) and dfs(root.right, root.val, rightBound)
            else:
                return False
        
        return dfs(root, float('-inf'), float('inf') )