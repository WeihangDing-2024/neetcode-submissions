# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def helper(node, res):
            if not node:
                res.append("#")
                return
            res.append("|" + str(node.val) + "|")
            helper(node.left, res)
            helper(node.right, res)
        
        helper(root, res)
        return "".join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        res = data.split("|")
        print(res)
        if data[0] == "#":
            return None

        i = 0
        j = i + 1
        while data[j] != "|":
            j += 1
        root_val = int(data[i+1:j])
        root = TreeNode(root_val)
        prev = root
        stk = [root]
        isLeft = True
        i = j + 1
        
        while i < len(data):
            if isLeft:
                if data[i] != "#":
                    j = i + 1
                    while data[j] != "|":
                        j += 1
                    node_val = int(data[i+1:j])
                    node = TreeNode(node_val)

                    prev.left = node
                    prev = node
                    stk.append(node)
                    i = j + 1
                else:
                    prev.left = None
                    isLeft = False
                    if stk:
                        prev = stk.pop()
                    i += 1
            else:
                if data[i] != "#":
                    j = i + 1
                    while data[j] != "|":
                        j += 1
                    node_val = int(data[i+1:j])
                    node = TreeNode(node_val)

                    prev.right = node
                    prev = node
                    stk.append(node)
                    i = j + 1
                    isLeft = True
                else:
                    prev.right = None
                    if stk:
                        prev = stk.pop()
                    i += 1
        return root