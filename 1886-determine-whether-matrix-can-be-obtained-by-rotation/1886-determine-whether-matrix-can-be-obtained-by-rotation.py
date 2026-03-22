class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        n = len(mat)
        
        def rotate(matrix):
            # transpose
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            # reverse each row
            for row in matrix:
                row.reverse()
        
        for _ in range(4):  # try all 4 rotations
            if mat == target:
                return True
            rotate(mat)
        
        return False
        