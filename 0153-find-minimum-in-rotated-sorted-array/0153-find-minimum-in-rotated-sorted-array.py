class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start = 0
        end = len(nums) -1
        
        res = nums[(start + end) // 2]

        while start <= end:
            if nums[start] < nums[end]:
                if nums[start] < res:
                    res = nums[start]

            mid = (start + end) // 2

            if nums[mid] < res:
                res = nums[mid]

            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
                 
        return res



        