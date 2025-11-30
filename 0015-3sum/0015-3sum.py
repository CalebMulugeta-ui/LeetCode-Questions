class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()


        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:   
                continue
                                       
            l = i+1
            r = len(nums) - 1

            while l < r:
                if l-1 != i:
                    if nums[l] == nums[l-1]:
                        l+=1
                        continue

                if r != len(nums)-1:
                    if nums[r] == nums[r+1]:
                        r-=1
                        continue

                if nums[i] + nums[l] + nums[r] > 0:
                    r-=1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
        return res
                
        return res


        