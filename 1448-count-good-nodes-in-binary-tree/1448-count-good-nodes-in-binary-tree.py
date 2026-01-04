# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, currMax):
            if not root:
                return 0
            
            if root.val >= currMax:
                res = 1
            else:
                res = 0
            
            currMax = max(root.val, currMax)

            res += dfs(root.left, currMax) + dfs(root.right, currMax)

            return res
        
        return dfs(root, root.val)
