class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t=="":
            return ""


        tMap = {}
        for i in t:
            tMap[i] = 1 + tMap.get(i,0)

        have,need=0,len(tMap)     
        
        L=0
        sMap = {}
        res = [-1,-1]
        length = float('inf')

        for R in range(len(s)):
            curr = s[R]
            sMap[curr] = sMap.get(curr, 0) + 1

            if curr in tMap and sMap[curr] == tMap[curr]:
                have+=1

            while have==need:
                if R-L+1 < length:
                    length = R-L+1
                    res = [L,R]

                sMap[s[L]]-=1
                if s[L] in tMap and sMap[s[L]] < tMap[s[L]]:
                    have-=1
                L+=1
                
        return s[res[0]:res[1]+1]


            
                


