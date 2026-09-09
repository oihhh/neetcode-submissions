class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}    
        for n in s:
            count[n] = 1 + count.get(n, 0)  
        for n in t:
            count[n] = count.get(n, 0) - 1 
        return all(v == 0 for v in count.values())




            

       



            
            
        