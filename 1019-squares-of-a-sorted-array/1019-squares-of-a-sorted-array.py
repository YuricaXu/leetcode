class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):#loop
            nums[i] *= nums[i]
        nums.sort()
        return nums 