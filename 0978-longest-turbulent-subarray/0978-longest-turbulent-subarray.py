class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        prev = ""
        total = 1
        L = 0
        R = 1
        while R < len(arr):
            if arr[R-1] > arr[R] and prev != ">":
                total = max(total, R-L+1)
                R+=1
                prev = ">"
            elif arr[R-1] < arr[R] and prev != "<":
                total = max(total, R-L+1)
                R+=1
                prev = "<"
            elif (arr[R-1] > arr[R] and prev == ">") or (arr[R-1] < arr[R] and prev == "<"):
                L = R-1
                prev =""
            else:
                L=R
                prev=""
                R+=1

        return total