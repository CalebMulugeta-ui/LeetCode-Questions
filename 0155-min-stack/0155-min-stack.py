class MinStack(object):

    def __init__(self):
        self.item = []

        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.item.append(val)

        

    def pop(self):
        """
        :rtype: None
        """
        del self.item[-1]



    def top(self):
        """
        :rtype: int
        """
        return self.item[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.item)
        


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()