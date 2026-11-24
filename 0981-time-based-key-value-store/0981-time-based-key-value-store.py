class TimeMap(object):

    def __init__(self):
        self.keyMap = defaultdict(list)


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.keyMap[key].append([value, timestamp])

        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        valueList = self.keyMap[key]
        l = 0
        r = len(valueList)-1

        while l <= r:
            mid = (l+r)//2
            if valueList[mid][1] == timestamp:
                return valueList[mid][0]
            elif valueList[mid][1] < timestamp:
                l = mid+1
            else:
                r = mid-1
        
        if l == 0:
            return ""
        else:
            mid = (l+r)//2
            return valueList[mid][0]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)