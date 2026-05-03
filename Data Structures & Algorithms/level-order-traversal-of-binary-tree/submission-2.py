# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        # def dfs(node: Optional[TreeNode], depth: int):
        #     if not node:
        #         return None
        #     if len(res) == depth:
        #         res.append([])
        #     res[depth].append(node.val)
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)
        # dfs(root, 0)
        # return res

        queue = collections.deque()
        queue.append(root)

        while queue:
            nc = len(queue)
            level = []
            while nc > 0:
                front = queue.popleft()
                if front:
                    level.append(front.val)
                    queue.append(front.left)
                    queue.append(front.right)
                nc -= 1
            if level:
                res.append(level)
        return res
        