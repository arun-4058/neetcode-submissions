# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # res = True
        # def dfs(root):
        #     nonlocal res
        #     if not root:
        #         return 0
        #     lh, rh = dfs(root.left), dfs(root.right)
        #     res = (res and abs(lh-rh) <= 1)
        #     return 1 + max(lh, rh)
        # dfs(root)
        # return res

        def dfs(root):
            if not root:
                return [True, 0]
            l, r = dfs(root.left), dfs(root.right)
            balanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1
            return [balanced, 1 + max(l[1], r[1])]
        return dfs(root)[0]
