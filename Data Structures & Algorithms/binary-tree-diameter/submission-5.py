# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[Tree]) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # d = self.height(root.left) + self.height(root.right)
        # sd = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        # return max(d, sd)

        res = 0
        def height(root):
            nonlocal res

            if not root:
                return 0
            lh, rh = height(root.left), height(root.right)
            res = max(res, lh+rh)  # update diameter
            return 1 + max(lh, rh)
        height(root)
        return res

        