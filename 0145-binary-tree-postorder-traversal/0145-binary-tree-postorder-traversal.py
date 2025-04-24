class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack1 = [root]     # First stack to process nodes
        stack2 = []         # Second stack to store postorder in reverse

        while stack1:
            node = stack1.pop()
            stack2.append(node.val)  # Store the node's value in stack2

            # Push left and right children into stack1
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        # Reverse stack2 to get the correct postorder traversal
        return stack2[::-1]