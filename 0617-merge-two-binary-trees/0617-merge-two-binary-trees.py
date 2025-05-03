
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#If at any node one tree is none then we just take the node of the other tree. If both tree nodes exist then we create a new node and then add A and B's values up.
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            res = TreeNode(root1.val + root2.val)
            res.left = self.mergeTrees(root1.left, root2.left)
            res.right = self.mergeTrees(root1.right, root2.right)
        
        return res

                