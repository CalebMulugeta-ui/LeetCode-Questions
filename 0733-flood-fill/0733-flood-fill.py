class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        #store start pixels color
        pixelColor = image[sr][sc]
        #create a dfs helper function, paratemeters: grid, starting pixel color, color, visitSet, sr, sc)
        def dfs(image, pixelColor, color, visited, sr, sc):
            ROWS, COLS = len(image), len(image[0])
            #base case: if r or c is out of bounds, or current color isnt equal to start pixel color, return grid
            if sr < 0 or sc < 0 or sr == ROWS or sc == COLS or image[sr][sc] != pixelColor or (sr,sc) in visited:
                return image
            
            image[sr][sc] = color
            visited.add((sr,sc))
            #otherwise, change curr element color, and then move left,rigtht, down up.
            dfs(image, pixelColor, color, visited, sr, sc + 1)
            dfs(image, pixelColor, color, visited, sr, sc - 1)
            dfs(image, pixelColor, color, visited, sr+1, sc)
            dfs(image, pixelColor, color, visited, sr-1, sc)

            return image

        return dfs(image,pixelColor,color, set(), sr, sc)
        