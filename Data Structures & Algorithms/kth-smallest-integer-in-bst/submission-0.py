# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        curr = 1
        visited = set()
        node = root

        while stk or node:
            while node:
                stk.append(node)
                node = node.left
            node = stk.pop()
            if curr == k:
                return node.val
            curr += 1
            node = node.right
            