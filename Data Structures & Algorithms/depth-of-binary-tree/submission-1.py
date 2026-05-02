# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(height(root.left), height(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        if not root:
            return 0
        q = collections.deque()
        q.append(root)
        d = 0
        while q:
            nc = len(q)
            while nc > 0:
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                nc -= 1
            d += 1
        return d
            


        
        