# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        
        arr = []

        def dfs(root, arr):
            if not root:
                return 

            arr.append(root.val)
            dfs(root.left, arr)
            dfs(root.right, arr)
        
        dfs(root,arr)

        sortArr = sorted(arr)
        #[1,2,3,4] k = 1

        return sortArr[k-1]

       