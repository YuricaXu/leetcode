class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        for index, value in enumerate(nums): 
            if target - value in records:   
    # Traverse the current element and check if the complement exists in the map
                 return [records[target - value], index]

# If no match is found, store the current value and its index in the map
            records[value] = index
        return []
