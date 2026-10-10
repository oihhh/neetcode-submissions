class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for a in s:
            count[a] = 1 + count.get(a, 0)
        for b in t:
            count[b] = count.get(b, 0) - 1
        return all(v == 0 for v in count.values())




            

       



            
            
        