# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        li = []
        curr = head
        
        while curr:
            li.append(curr)
            curr = curr.next

        l = 0
        r = len(li) - 1

        while l < r:
            li[l].next = li[r]
            l+=1
            li[r].next = li[l]
            r-=1
        li[l].next = None
         
        return head
        