class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        # Create a hash map to store the frequency of elements in nums1
        for num in nums1:
            table[num] = table.get(num, 0) + 1
    
        res = set()
        for num in nums2:
            # If the number from nums2 exists in the table (i.e., also in nums1)
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res) 