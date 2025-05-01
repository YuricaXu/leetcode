class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        q=0#the maxium sum of 1
        p=0#current sum
        for i in nums:
            if i == 1:
                p+=1
                q=max(p,q)
            else:
                p=0
        return q