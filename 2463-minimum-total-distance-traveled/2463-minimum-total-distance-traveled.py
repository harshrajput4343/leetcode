class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(i, j, used):
            # i -> robot index
            # j -> factory index
            # used -> how many robots used in current factory
            
            if i == len(robot):
                return 0
            
            if j == len(factory):
                return float('inf')
            
            pos, limit = factory[j]
            
            # Option 1: skip this factory
            res = dp(i, j + 1, 0)
            
            # Option 2: assign current robot if limit allows
            if used < limit:
                res = min(
                    res,
                    abs(robot[i] - pos) + dp(i + 1, j, used + 1)
                )
            
            return res
        
        return dp(0, 0, 0)
        