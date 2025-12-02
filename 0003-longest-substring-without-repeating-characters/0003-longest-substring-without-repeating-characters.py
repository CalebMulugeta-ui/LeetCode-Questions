class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        mySet = set()
        myList = []

        for i in range(len(s)):
            lengthSub = 0
            for e in range(i, len(s)):

                if s[e] in mySet:
                    mySet.clear()
                    myList.append(lengthSub)
                    break

                mySet.add(s[e])
                lengthSub+=1

            myList.append(lengthSub)

        if myList:
            return max(myList)
        else:
            return 0
                