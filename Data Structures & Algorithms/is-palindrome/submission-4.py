class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = "".join(char.lower() for char in s if char.isalnum())
        if clean_string == clean_string[::-1]:
            return True
        else:
            return False