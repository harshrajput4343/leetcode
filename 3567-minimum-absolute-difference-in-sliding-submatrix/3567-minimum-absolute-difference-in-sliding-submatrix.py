
class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        rows = m - k + 1
        cols = n - k + 1
        
        ans = [[0] * cols for _ in range(rows)]
        
        # Iterate over every possible top-left corner of a k×k submatrix
        for i in range(rows):
            for j in range(cols):
                
                # Collect all values in the k×k submatrix
                values = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        values.append(grid[r][c])
                
                # Remove duplicates and sort
                # Sorting is key: min absolute diff is always between adjacent elements
                unique_vals = sorted(set(values))
                
                # If all elements are the same, diff = 0 (already default)
                if len(unique_vals) == 1:
                    ans[i][j] = 0
                    continue
                
                # Find minimum absolute difference between consecutive sorted values
                min_diff = float('inf')
                for idx in range(1, len(unique_vals)):
                    diff = unique_vals[idx] - unique_vals[idx - 1]  # always >= 0 after sort
                    if diff < min_diff:
                        min_diff = diff
                
                ans[i][j] = min_diff
        
        return ans