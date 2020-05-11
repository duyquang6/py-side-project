class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old = image[sr][sc]
        if old == newColor: return image
        image[sr][sc] = newColor
        lst = [ [sr+x,sc+y]  for x,y in [[-1, 0], [0, -1], [1, 0], [0,1]]]
        newPts = filter(lambda x: x[0] >= 0 and x[1] >= 0 and x[0] < len(image) and x[1] < len(image[0]) and image[x[0]][x[1]] == old, lst)
        for x,y in newPts:
            self.floodFill(image, x,y, newColor)
        return image