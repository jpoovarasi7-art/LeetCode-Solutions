from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Add the baseline boundary conditions
        restrictions.append([1, 0])
        
        # Sort restrictions based on building index
        restrictions.sort()
        
        # If the last building is not explicitly capped, add a theoretical limit boundary
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
            
        m = len(restrictions)
        
        # Pass 1: Forward propagation (left to right)
        # A building's height cannot exceed its predecessor's height + the index gap
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + dist)
            
        # Pass 2: Backward propagation (right to left)
        # A building's height cannot exceed its successor's height + the index gap
        for i in range(m - 2, -1, -1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + dist)
            
        # Pass 3: Find peak heights between all adjacent restriction intervals
        max_height = 0
        for i in range(m - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i + 1]
            dist = id2 - id1
            
            # Mathematical peak calculation between two valid boundaries
            peak = (h1 + h2 + dist) // 2
            max_height = max(max_height, peak)
            
        return max_height
