# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.helper(root, 0, res)
        return res[0]

    def helper(self, root, curr_depth, max_depth):
        if not root:
            max_depth[0] = max(max_depth[0], curr_depth)
            return
        self.helper(root.left, curr_depth + 1, max_depth)
        self.helper(root.right, curr_depth + 1, max_depth)
        