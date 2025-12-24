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
        def dfs(root,count):
            if not root:
                return count

            count += 1
            leftDepth = dfs(root.left, count)
            rightDepth = dfs(root.right, count)
            return max(leftDepth, rightDepth)
            
        count = 0
        return dfs(root,count)

        
 

        

        