# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        queue = deque()
        finalList = []
        if root:
            queue.append(root)

        while len(queue)>0:
            rightMost = 0
            for i in range(len(queue)):
                rightMost = queue.popleft()

                if rightMost.left:
                    queue.append(rightMost.left)
                if rightMost.right:
                    queue.append(rightMost.right)
            finalList.append(rightMost.val)

        return finalList

        