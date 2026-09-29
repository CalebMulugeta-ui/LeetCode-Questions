class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hsh = {}

        for i in range(len(nums)):
            if nums[i] not in hsh:
                hsh[target - nums[i]] = i
            else:
                return [hsh[nums[i]], i]

                

            

                   