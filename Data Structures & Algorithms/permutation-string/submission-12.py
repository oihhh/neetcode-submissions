class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        count_A = {}
        count_B = {}
        for i in s1:
            count_A[i] = 1 + count_A.get(i, 0)
        for r in range(len(s2)):
            count_B[s2[r]] = 1 + count_B.get(s2[r], 0)

            while r - l + 1 == len(s1):
                if count_A == count_B:
                    return True
                count_B[s2[l]] -= 1
                if count_B[s2[l]] == 0:
                    del count_B[s2[l]]
                l += 1

        return False
        

#does the while loop runs right after the len(window) == len(s1) or does it check and runs in the next loop.
        