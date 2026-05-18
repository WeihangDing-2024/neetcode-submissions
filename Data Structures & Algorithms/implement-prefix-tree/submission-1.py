class PrefixTree:

    def __init__(self): 
        self.trie = [{}, False]
        # {'a': {}, true; 'b': 2}

    def insert(self, word: str) -> None:
        curr_pos = self.trie[0]
        for i, char in enumerate(word):
            if char not in curr_pos:
                curr_pos[char] = [{}, False]
            if i == len(word) - 1:
                curr_pos[char][1] = True
            else:
                curr_pos = curr_pos[char][0]

    def search(self, word: str) -> bool:
        curr_pos = self.trie[0]
        for i, char in enumerate(word):
            if char not in curr_pos:
                return False
            if i == len(word) - 1:
                return curr_pos[char][1]
            curr_pos = curr_pos[char][0]
        return False # should not reach this line        

    def startsWith(self, prefix: str) -> bool:
        curr_pos = self.trie[0]
        for i, char in enumerate(prefix):
            if char not in curr_pos:
                return False
            curr_pos = curr_pos[char][0]
        return True
        
        