class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True


    def search(self, word: str) -> bool:

        def helper(word, node):
            curr = node
            for i, char in enumerate(word):
                if char == '.':
                    for key, item in curr.children.items():
                        new_word = word[i+1:]
                        if helper(new_word, item):
                            return True
                    return False
                if not char in curr.children:
                    return False
                curr = curr.children[char]
            return curr.endOfWord
        
        return helper(word, self.root)





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)