class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end:                

            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

        #check if ur in the left or right portion
            #in the left 
            if nums[mid] >= nums[start]:
                if target > nums[mid] or nums[start] > target :
                    start = mid + 1
                else:
                    end = mid - 1
                    
            #in the right
            else:
                if target < nums[mid] or target > nums[end] :
                    end = mid - 1
                else:
                    start = mid + 1

                
        return -1




        return -1


        