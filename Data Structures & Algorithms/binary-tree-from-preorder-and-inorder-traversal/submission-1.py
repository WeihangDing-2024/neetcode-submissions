# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        look_up = {}
        for i, val in enumerate(inorder):
            look_up[val] = i

        def helper(preorder, p_s, p_e, inorder, i_s):
            if p_s > p_e:
                return None
            node_val = preorder[p_s]
            node = TreeNode(node_val)

            left_end = look_up[node_val]
            left_length = left_end - i_s

            node.left = helper(preorder, p_s+1, p_s+left_length, inorder, i_s)
            node.right = helper(preorder, p_s+left_length + 1, p_e, inorder, i_s + left_length + 1)
            return node
        return helper(preorder, 0, len(preorder) - 1, inorder, 0)
        