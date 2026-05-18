# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []        

        q = deque()
        q.append(root)

        while q:
            q_len = len(q)
            right_node = None
            for _ in range(q_len):
                curr = q.popleft()
                if curr:
                    if not right_node:
                        right_node = curr
                    q.append(curr.right)
                    q.append(curr.left)
            if right_node:
                res.append(right_node.val)
        return res     
        