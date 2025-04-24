class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        current = root

        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left

            # Current is None at this point
            current = stack.pop()
            result.append(current.val)  # Visit the node

            # Visit the right subtree
            current = current.right

        return result