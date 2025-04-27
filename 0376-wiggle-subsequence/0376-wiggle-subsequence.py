class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return len(nums)#if the length is 0 or 1
        curDiff =0#current difference
        preDiff =0#previou differen
        result =1
        for i in range(len(nums)-1):
            curDiff = nums[i+1]-nums[i]
            if curDiff ==0:
              continue
            if preDiff==0 or preDiff * curDiff <= 0:
               result += 1
               preDiff = curDiff
        return result