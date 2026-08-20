class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:

             
 
            anagram_key = "".join(sorted(word))
            anagram_map[anagram_key].append(word)
        return list(anagram_map.values())

            
        