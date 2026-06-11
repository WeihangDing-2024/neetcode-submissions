# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        stk = [(root, 1)]
        res = 1

        while stk:
            curr, depth = stk.pop()
            res = max(res, depth)
            if curr.left:
                stk.append((curr.left, depth + 1))
            if curr.right:
                stk.append((curr.right, depth + 1))
        return res
