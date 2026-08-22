class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in matrix:
            left, right = 0, len(i) - 1
            if i[right] >= target:
                while left <= right:
                    mid = left + (right - left) // 2
                    if i[mid] == target:
                        return True
                    elif i[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1 
        return False 