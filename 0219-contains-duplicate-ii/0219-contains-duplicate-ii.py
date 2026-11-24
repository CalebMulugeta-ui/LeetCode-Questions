class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        windowSet = set()
        L = 0
        
        for R in range(len(nums)):
            if abs(R-L) > k:
                windowSet.remove(nums[L])
                L+=1
            
            if nums[R] in windowSet:
                return True
            
            windowSet.add(nums[R])
        
        return False

        