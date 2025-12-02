class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestSub = 0

        for i in range(len(s)):
            mySet = set()
            mySet.add(s[i])

            for e in range(i+1, len(s)):
                if s[e] not in mySet:
                    mySet.add(s[e])
                else:
                    longestSub = max(longestSub, len(mySet))
                    break

            longestSub = max(longestSub, len(mySet))

        return longestSub
                