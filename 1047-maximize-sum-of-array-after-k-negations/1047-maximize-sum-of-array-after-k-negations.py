class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x:abs(x), reverse=True)#First Step:sort nums

        for i in range(len(nums)):#Step 2
            if nums[i]<0 and k>0 :
                nums[i]*=-1
                k-=1
        if k%2 ==1:#Step 3,after one turn
           nums[-1]*=-1

        result=sum(nums)
        return result