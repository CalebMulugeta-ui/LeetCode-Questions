class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjMap = {}
        for src, dst in prerequisites:
            if src not in adjMap:
                adjMap[src] = []
            if dst not in adjMap:
                adjMap[dst] = []
            adjMap[src].append(dst)
        
        visit = set()
        def dfs(crs): 
            if crs in visit:
                return False

            if adjMap[crs] == []:
                return True 

            visit.add(crs)
            for preq in adjMap[crs]:
                if not dfs(preq):
                    return False
            
            visit.remove(crs)
            adjMap[crs] = []
            return True

        
        for crs in range(numCourses):
            if crs in adjMap:
                if not dfs(crs):
                    return False
        return True
        