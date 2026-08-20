class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        brackets_map = { ")": "(", "}": "{", "]": "["}
        for i in s:
            if i in brackets_map:
                if brackets and brackets[-1] == brackets_map[i]:
                    brackets.pop()
                else:
                    return False
            else:
                brackets.append(i)
        return True if not brackets else False

       

        