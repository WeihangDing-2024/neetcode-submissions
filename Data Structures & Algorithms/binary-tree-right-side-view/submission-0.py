# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        node_dict = defaultdict(list)
        curr_level = 0
        node_dict[0].append(root)

        while node_dict[curr_level]:
            node_lst = node_dict[curr_level]
            found_rightmost = False
            for i in range(0, len(node_lst)):
                # append from right to left
                if node_lst[i]:
                    if not found_rightmost:
                        res.append(node_lst[i].val)
                        found_rightmost = True
                    node_dict[curr_level+1].append(node_lst[i].right)
                    node_dict[curr_level+1].append(node_lst[i].left)
            curr_level += 1
        
        return res
        