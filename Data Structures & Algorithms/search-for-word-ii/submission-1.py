class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res_set = set()

        # build word Trie
        def addWord(word, root):
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.endOfWord = True
        
        root = TrieNode()
        for word in words:
            addWord(word, root)
        
        # dfs to find prefix
        def dfs(i, j, node, curr_char_lst):
            curr = node

            # success: found a word
            if curr.endOfWord:
                res_set.add("".join(curr_char_lst))
                curr.endOfWord = False
            
            # failure: out of range
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return

            # failure: visited
            if board[i][j] == "#":
                return

            # process to next cell
            char = board[i][j]
            if char not in curr.children:
                return
            
            board[i][j] = "#"
            next_node = curr.children[char]
            curr_char_lst.append(char)

            # dfs
            dfs(i+1, j, next_node, curr_char_lst)
            dfs(i-1, j, next_node, curr_char_lst)
            dfs(i, j+1, next_node, curr_char_lst)
            dfs(i, j-1, next_node, curr_char_lst)

            # pruning
            if not next_node.children:
                del curr.children[char]

            # revert the change
            curr_char_lst.pop()
            board[i][j] = char
            return



        # main loop
        # res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not dfs(i, j, root, []):
                    continue
        res = list(res_set)
        return res

        