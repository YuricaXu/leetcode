class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        """
        :type nums: List[int]
        :rtype: int
        """

        new_nums = sorted(nums , reverse = True)
        largest = max(nums)

        if (largest >= 2 * new_nums[1]):
            return nums.index(largest)
        return -1
