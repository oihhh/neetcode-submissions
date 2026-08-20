class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in strs:
            key = [0] * 26 
            for c in i:
                key[ord(c) - ord('a')] += 1
            group[tuple(key)].append(i)
        return list(group.values())
       
        