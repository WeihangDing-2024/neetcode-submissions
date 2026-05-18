# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # curr_max = float('inf')
        stk = [(root, float('inf'), float('-inf'))]
        
        while stk:
            node, curr_max, curr_min = stk.pop()
            if node.val >= curr_max or node.val <= curr_min:
                return False
            if node.left:
                stk.append((node.left, node.val, curr_min))
            if node.right:
                stk.append((node.right, curr_max, node.val))
        
        return True
        
        
        