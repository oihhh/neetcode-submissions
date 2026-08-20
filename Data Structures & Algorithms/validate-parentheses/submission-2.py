class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        closeToOpen = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in closeToOpen:
                if brackets and brackets[-1] == closeToOpen[i]:
                    brackets.pop()
                else:
                    return False
            else:
                brackets.append(i)
        return True if not brackets else False
                
       

        