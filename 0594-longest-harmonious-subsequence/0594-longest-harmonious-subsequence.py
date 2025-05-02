class Solution:
    def findLHS(self, nums: List[int]) -> int:

        #Approach 1
        # Brute Force Approach 
        # intitally sort the array
        # find the max_len of the intergers where difference is 1 and count is max_
        #let's work on that
        # nums.sort() #nlog(n) >> complexity
        # '''Input: [2,3,1,4,1,3,1]
        #    Output: [1,1,1,2,3,3,4]'''
        # max_ = 0
        # for i in range(len(nums)): #>> O(n)
        #     count = 1
        #     for j in range(i +1, len(nums)): #>> O(n)
        #         if nums[j] == nums[i] or abs(nums[i] - nums[j]) == 1:
        #             count += 1
        #         else:
        #             break
        #     if nums[i] == nums[i + count-1]: # condition for same number in the array
        #         count = 0
        #     max_ = max(count , max_)

        # return max_
        #the above appraoch is o(n^2) which is not suitable for the large testcases
        # optimize the same:
        # Maitaining the dict_
        dict_ = Counter(nums)
        # dict_.sort()
        max_ = 0
        
        for k, v in dict_.items():
            count = 0
            if k+1 in dict_:
                count = dict_[k] + dict_[k+1]
            max_ = max(max_, count)
        return max_
        



