class Solution:
    def distance (self, x1, x2, y1, y2, radius):
        return (((x1 - x2) ** 2 + (y1 - y2) ** 2)**.5) <= radius
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        min_x = min(x1,x2)
        max_x = max(x1,x2)
        min_y = min(y1,y2)
        max_y = max(y1,y2)

        closest_x = max(min_x, min(xCenter, max_x)) 
        closest_y = max(min_y, min(yCenter, max_y))
        return self.distance(closest_x, xCenter, closest_y, yCenter, radius)

if __name__ == '__main__':
    solution = Solution()
    result = solution.checkOverlap(radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1)
    print(result)