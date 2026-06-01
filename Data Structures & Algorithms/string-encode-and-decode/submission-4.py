class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word))+"#"+word)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            res.append(s[j+1:j+1+word_len])
            i = j+1+word_len
        return res

