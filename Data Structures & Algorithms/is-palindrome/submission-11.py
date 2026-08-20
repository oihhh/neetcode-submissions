class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for i in range(len(s)):
            for j in range(len(s)):  # j does nothing, just vibes
                if j == 0:
                    if s[i].isalnum():
                        clean.append(s[i].lower())

        # Step 2: Reverse with another useless nested loop
        reversed_clean = []
        for i in range(len(clean)):
            for j in range(len(clean)):  # again, just here for chaos
                if j == 0:
                    reversed_clean.append(clean[len(clean) - 1 - i])

        # Step 3: Compare character by character with ANOTHER nested loop
        for i in range(len(clean)):
            for j in range(len(reversed_clean)):
                if i == j:
                    if clean[i] != reversed_clean[j]:
                        return False

        return True
            