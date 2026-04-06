class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Convert obstacles list to set for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        
        # Directions: North, East, South, West
        # Represented as (dx, dy)
        directions = [
            (0, 1),   # North
            (1, 0),   # East
            (0, -1),  # South
            (-1, 0)   # West
        ]
        
        # Start at origin facing North
        x, y = 0, 0
        direction = 0  # index in directions array
        
        max_distance = 0
        
        for command in commands:
            if command == -1:
                # Turn right: move clockwise
                direction = (direction + 1) % 4
                
            elif command == -2:
                # Turn left: move anti-clockwise
                direction = (direction - 1) % 4
                
            else:
                # Move forward step-by-step
                dx, dy = directions[direction]
                
                for _ in range(command):
                    next_x = x + dx
                    next_y = y + dy
                    
                    # Check obstacle BEFORE moving
                    if (next_x, next_y) in obstacle_set:
                        break  # stop moving for this command
                    
                    # Safe to move
                    x, y = next_x, next_y
                    
                    # Update max squared distance
                    max_distance = max(max_distance, x*x + y*y)
        
        return max_distance