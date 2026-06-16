# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for i, val in enumerate(inorder):
            indices[val] = i
        
        def dfs(p_s, p_e, i_s):
            if p_s > p_e:
                return None
            node_val = preorder[p_s]
            root = TreeNode(node_val)
            idx = indices[node_val]
            left_length = idx - i_s
            root.left = dfs(p_s+1, p_s+left_length, i_s)
            root.right = dfs(p_s+left_length+1, p_e, idx+1)
            return root
        
        return dfs(0, len(preorder) - 1, 0)
            
        