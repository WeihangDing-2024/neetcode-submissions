# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[]]
        max_level = 0
        stk = [(root, 0)]
        while stk:
            curr, level = stk.pop()
            if level > max_level:
                res.append([])
                max_level += 1
            res[level].append(curr.val)
            if curr.right:
                stk.append((curr.right, level + 1))
            if curr.left:
                stk.append((curr.left, level + 1))
            
        return res            
        