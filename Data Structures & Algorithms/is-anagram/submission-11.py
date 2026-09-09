class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = 0
        count_a = {}
        count_b = {}
        for a in s:
            
            while l < len(t):
                for r in t:
                    count_b[r] = 1 + count_b.get(r, 0)
                    l += 1
            
            count_a[a] = 1 + count_a.get(a, 0)
        
        return count_a == count_b





            

       



            
            
        