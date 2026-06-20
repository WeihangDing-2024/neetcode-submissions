# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_lst = data.split(",")
        idx = [0]

        def dfs():
            i = idx[0]
            if data_lst[i] == "N":
                idx[0] = i + 1
                return None
            node_val = data_lst[i]
            node = TreeNode(node_val)
            idx[0] = i + 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()            


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))