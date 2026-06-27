class PrefixTree:

    def __init__(self):
        self.children = {}
        self.endOfWord = False
        

    def insert(self, word: str) -> None:
        curr = self
    
        for char in word:
            children = curr.children
            if not char in children:
                children[char] = PrefixTree()
            curr = children[char]

        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self
        for char in word:
            children = curr.children
            if not char in children:
                return False
            curr = children[char]
        return curr.endOfWord


    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            children = curr.children
            if not char in children:
                return False
            curr = children[char]
        return True
        