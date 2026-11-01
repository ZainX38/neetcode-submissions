class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Algorithm:
                    - Loop through nums
                    - Create a list to track numbers we have seen
                    - If num is inside list -> Duplicate
                    - If num is not inside dictionary -> Save into list
        '''

        # Can't use list as when we use the if statement later, 
        # it will look through every element one by one --> Time Complexity becomes O(n^2)
        # But a set uses hashing --> Computer runs a hash function and knows exactly 
        # where the number is in memory = O(1) to lookup which means O(n) time complexity
        tracker = set()


        for i in range(len(nums)):
            if nums[i] in tracker:
                return True
                
            tracker.add(nums[i])
        return False