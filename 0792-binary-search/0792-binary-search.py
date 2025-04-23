class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)-1#define target[left,right]

        while left<=right:
            middle=left+(right-left)//2

            if nums[middle]>target:
                right=middle-1#[left,middle-1]
            elif nums[middle]<target:
                left=middle+1#[middle+1,right]
            else:
                return middle
        return -1#not find target