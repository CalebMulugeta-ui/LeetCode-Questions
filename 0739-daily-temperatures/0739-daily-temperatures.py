class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        myStack = [] #pair ()
        wamerDays = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while myStack and v > myStack[-1][0]:
                stackT, stackI = myStack.pop()
                wamerDays[stackI] = (i - stackI)

            myStack.append([v,i])
            

        return wamerDays



