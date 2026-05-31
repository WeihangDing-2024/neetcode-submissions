class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for word in strs:
            res.append(str(len(word)) + "#" + word)
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != "#":
                j += 1
            word_count = int(s[i:j])
            word = s[j+1:j+1+word_count]
            res.append(word)
            i = j+1+word_count
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))