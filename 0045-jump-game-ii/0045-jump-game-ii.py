class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1: #one 
            return 0
        i=0
        count=0
        cover=0

        while i<= cover:
            for i in range(i,cover+1):
                cover = max(nums[i]+i, cover)
                if cover >= len(nums)-1:
                    return count+1
            count +=1  