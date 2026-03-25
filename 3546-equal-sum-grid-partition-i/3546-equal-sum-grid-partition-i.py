class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total_sum = sum(sum(row) for row in grid)

        # must be even
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        # ----- horizontal cuts -----
        running = 0
        for i in range(m - 1):  # ensure bottom part is non-empty
            running += sum(grid[i])
            if running == target:
                return True

        # ----- vertical cuts -----
        running = 0
        for j in range(n - 1):  # ensure right part is non-empty
            col_sum = 0
            for i in range(m):
                col_sum += grid[i][j]

            running += col_sum
            if running == target:
                return True

        return False
        