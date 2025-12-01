class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        largestArea = 0
        l = 0
        r = len(height) -1

        while l < r:
            smallerBar = 0
            tempL = l
            tempR = r
            if height[l] < height[r]:
                smallerBar = height[l]
                l += 1
            else:
                smallerBar =  height[r]
                r-=1

            area = smallerBar * (tempR-tempL)

            if area > largestArea:
                largestArea = area
            
        return largestArea