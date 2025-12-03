class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0

        l = 0
        r = 0

        for r in range(len(s)):

            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            if (r - l + 1) - (max(count.values())) <= k:
                res = r - l + 1
                r += 1
            else:
                count[s[l]] -= 1
                l+=1

        return res