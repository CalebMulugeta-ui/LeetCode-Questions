class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        
        L=0
        res = 0
        avgSub = 0
        for R in range(len(arr)):
            if R-L+1 <= k:
                avgSub += arr[R]
            
            if R-L+1 == k:
                avg = avgSub/k
                if avg >= threshold:
                    res+=1
                avgSub -= arr[L]
                L+=1
        
        return res
        