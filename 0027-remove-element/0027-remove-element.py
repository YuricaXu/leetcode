class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast=0#fast
        slow=0#slow
        size=len(nums)
        while fast<size:
            if nums[fast]!= val:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow