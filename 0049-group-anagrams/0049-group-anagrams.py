class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = defaultdict(list)
        for i in strs:
            sample="".join(sorted(i.lower()))
            anagram_map[sample].append(i)
        
        return list(anagram_map.values())    


