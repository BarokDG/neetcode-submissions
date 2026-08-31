class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        mid = (top + bottom) // 2

        while top < bottom - 1:
            row = matrix[mid]
            if row[0] > target:
                bottom = mid
            elif row[0] < target:
                top = mid
            else:
                return True

            mid = (top + bottom) // 2

        if target == matrix[bottom][0]:
            return True
        elif target > matrix[bottom][0]:
            top = bottom
        
        l, r = 0, len(matrix[0]) - 1
        row_mid = (l + r) // 2
        while l <= r:
            if target > matrix[top][row_mid]:
                l = row_mid + 1
            elif target < matrix[top][row_mid]:
                r = row_mid - 1
            else:
                return True

            row_mid = (l + r) // 2

        return False

            
            