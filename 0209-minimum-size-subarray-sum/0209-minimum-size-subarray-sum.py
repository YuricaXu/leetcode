class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=len(nums)
        left=0
        right=0
        min_len=float('inf')
        cur_sum=0#current value

        while right < l :
            cur_sum+=nums[right]

            while cur_sum >= target:#while sum > current
                min_len=min(min_len, right-left+1)
                cur_sum-=nums[left]
                left+=1
            right+=1
        return min_len if min_len != float('inf') else 0