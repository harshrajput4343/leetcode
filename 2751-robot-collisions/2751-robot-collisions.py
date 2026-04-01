from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        
        # Step 1: sort by position
        robots = sorted(
            [(positions[i], healths[i], directions[i], i) for i in range(n)]
        )
        
        stack = []  # indices of robots (in robots array) moving right
        alive = [True] * n  # track survival
        curr_health = [h for _, h, _, _ in robots]
        
        for i in range(n):
            pos, h, d, original_idx = robots[i]
            
            if d == 'R':
                stack.append(i)
            else:  # d == 'L'
                while stack:
                    j = stack[-1]  # last R robot
                    
                    if curr_health[j] < curr_health[i]:
                        # R dies
                        alive[j] = False
                        stack.pop()
                        curr_health[i] -= 1
                    elif curr_health[j] > curr_health[i]:
                        # L dies
                        alive[i] = False
                        curr_health[j] -= 1
                        break
                    else:
                        # both die
                        alive[j] = False
                        alive[i] = False
                        stack.pop()
                        break
                else:
                    # no R to collide with → survives
                    pass
        
        # Step 2: collect survivors in original order
        result = []
        for i in range(n):
            if alive[i]:
                result.append((robots[i][3], curr_health[i]))
        
        result.sort()  # sort by original index
        return [h for _, h in result]
        