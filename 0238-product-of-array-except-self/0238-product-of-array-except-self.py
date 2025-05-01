class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1 for _ in range(size)]#copy nums

        left = 1
        for i in range(size):
            res[i] *= left
            left *= nums[i]

        right = 1
        for i in range(size-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res