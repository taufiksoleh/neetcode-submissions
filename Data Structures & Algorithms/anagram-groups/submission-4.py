class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for s in strs:
            az = [0] * 26 # a-z -> 26 character
            for c in s:
                az[ord(c) - ord('a')] += 1
            result[tuple(az)].append(s)
        return list(result.values())