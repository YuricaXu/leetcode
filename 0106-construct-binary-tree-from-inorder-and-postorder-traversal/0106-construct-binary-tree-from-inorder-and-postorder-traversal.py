class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        #  树为空. (递归终止条件)
        if not postorder:
            return None

        # 后序遍历的最后一个就是当前的中间节点.
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 找切割点.
        separator_idx = inorder.index(root_val)

        # 切割inorder数组. 得到inorder数组的左,右半边.
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx + 1:]

        #  切割postorder数组. 得到postorder数组的左,右半边.
        #  中序数组大小一定跟后序数组大小是相同的.
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left): len(postorder) - 1]

        #  递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
         # 返回答案
        return root
        