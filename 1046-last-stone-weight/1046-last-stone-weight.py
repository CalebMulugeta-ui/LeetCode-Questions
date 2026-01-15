class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        while len(stones) > 1:

            stones.sort(reverse = True)

            x = stones[0] #bigger
            y = stones[1] #smaller

            if x == y:
                stones.pop(0)
                stones.pop(0)
            else:
                stones.pop(1)
                stones[0] -= y
                

        if stones:
            return stones[0]
        else:
            return 0

                    



