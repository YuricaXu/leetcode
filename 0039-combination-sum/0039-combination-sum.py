from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(idx, ds, target):
            if target == 0:
                res.append(ds[:])
                return
            if idx == len(candidates):
                return
            if candidates[idx] <= target:
                ds.append(candidates[idx])  
                helper(idx, ds, target - candidates[idx])
                ds.pop()  # backtrack
            helper(idx + 1, ds, target)  

        res = []
        helper(0, [], target)
        return res