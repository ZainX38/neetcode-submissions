class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Each row covers a range [row[0], row[-1]], and the ranges are in
        increasing order with no overlap.

        1. Binary search over the rows to find the one whose range holds target:
             - target < row[0]  -> answer is in a row above, move up
             - target > row[-1] -> answer is in a row below, move down
             - otherwise        -> this is the only possible row, stop
        2. If no row's range holds target, return False.
        3. Binary search inside that row for the exact value.

        Time:  O(log m + log n) = O(log(m * n))
        Space: O(1)
        '''

        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2   # Get middle row

            if target < matrix[row][0]:
                # target is smaller than everything in this row, 
                # so it can only be in the row above
                bottom = row - 1
            
            elif target > matrix[row][-1]:
                # target is bigger than everything in this row, 
                # so it can only be in the row below
                top = row + 1
            
            else:
                # row[0] <= target <= row[-1]: this is the only row it could be in.
                # break leaves top and bottom unchanged, so top <= bottom stays True
                break

        # If the loop ended with top passing bottom, no row's range has the target
        if not (top <= bottom):
            return False


        # Binary seach row
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False