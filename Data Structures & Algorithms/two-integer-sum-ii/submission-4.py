class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            combined = numbers[l] + numbers[r]

            if combined > target:
                r -= 1
            elif combined < target:
                l += 1
            elif combined == target:
                return [l + 1, r + 1]
        