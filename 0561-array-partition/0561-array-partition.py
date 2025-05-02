class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)#sorting
        res = 0
        n = len(nums)

        for idx in range(0, n, 2):#add
            res += sorted_nums[idx]
        
        return res