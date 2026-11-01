class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Algorithm:
                    - Loop through nums
                    - Create a list to track numbers we have seen
                    - If num is inside list -> Duplicate
                    - If num is not inside dictionary -> Save into list
        '''

        tracker = []

        for i in range(len(nums)):
            if nums[i] in tracker:
                return True
            else:
                tracker.append(nums[i])
        return False