# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root):
        self.tilt_sum = 0
        def DFS(root):
            if not root: return 0
            left_sum, right_sum = DFS(root.left), DFS(root.right)
            self.tilt_sum += abs(left_sum - right_sum)
            return left_sum + right_sum + root.val
        DFS(root)
        return self.tilt_sum       