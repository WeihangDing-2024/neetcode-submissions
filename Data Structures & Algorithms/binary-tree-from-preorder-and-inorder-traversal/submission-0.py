# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        curr_val = preorder[0]
        root = TreeNode(curr_val)
        idx = inorder.index(curr_val)
        
        root.left = self.buildTree(preorder[1:1+idx], inorder[0:idx])
        root.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        return root
    
        