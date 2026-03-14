class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # points = [[1,1],[3,4],[-1,0]]
        res = 0

        x1 , y1 = points.pop() # 1,4

        while points:
            x2,y2 = points.pop()  # 3,4 only -1, 0 left in points
            res += max(abs(y2 - y1), abs(x2 - x1))
            x1,y1 = x2,y2

        return res