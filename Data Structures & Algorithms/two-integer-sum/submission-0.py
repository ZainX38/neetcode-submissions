class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        solution = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    solution.append(i)
                    solution.append(j)

                    nums.remove(nums[i])
                    # The size of the list decreases as we removed one already,
                    # So, j moves one position down
                    nums.remove(nums[j-1])  
                    break

        return solution
        