class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        adjMap = {}
        for i in range(numCourses):
            adjMap[i] = []

        for crs,preq in prerequisites:
            adjMap[crs].append(preq)

        order = []
        orderSet = set()
        visit = set()

        def dfs(crs):

            if adjMap[crs] == []:
                if crs not in orderSet:
                    order.append(crs)
                    orderSet.add(crs)
                    return True
                return True
            
            if crs in visit:
                return False
            
            visit.add(crs)
            for preq in adjMap[crs]:
                if not dfs(preq):
                    return False
            
            order.append(crs)
            orderSet.add(crs)
            visit.remove(crs)
            adjMap[crs] = []
            return True

      
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return order




        

        
        
        