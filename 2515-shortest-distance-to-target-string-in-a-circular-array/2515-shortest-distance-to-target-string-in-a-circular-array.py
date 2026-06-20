class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = n
        found = False
    
        for i in range(n):
            if words[i] == target:
                found = True
            # Distance going one way
                abs_dist = abs(i - startIndex)
            # Distance going the other way (circular)
                dist = min(abs_dist, n - abs_dist)
                min_dist = min(min_dist, dist)
            
        return min_dist if found else -1