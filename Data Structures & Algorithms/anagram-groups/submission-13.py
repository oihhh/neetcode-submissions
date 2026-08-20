class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[int]:
        res = defaultdict(list)
        for i in strs:
            group = [0] * 26
            for c in i:
                group[ord(c) - ord('a')] += 1
            res[tuple(group)].append(i)
        return list(res.values())
        