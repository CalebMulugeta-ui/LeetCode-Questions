import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        #go thru the array of points calculating the distane
        #if our heap is smaller than K, push  [-currDistance, x, y], the reason for using the -distance is becuase, python doesnt have a maxHeap only min heap, therefore if you want a maxHeap, just track the of the bigger negative version of the numbers
        #the closer the distance the smaller the number
        #Have a max heap of length k

        h = []

        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            item = [-distance, x ,y]
            if len(h) < k:
                heappush(h, item)
            else:
                if item[0] > h[0][0]:
                    heapreplace(h, item)
        
        return [[x,y] for _ , x,y in h]


        