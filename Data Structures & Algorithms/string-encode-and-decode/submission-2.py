class Solution:
    

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for word in strs:
            res += str(len(word)) + "/" + word
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []

        i = 0
        while i < len(s):
            # deal with one word in one iteration
            length = ''
            while i < len(s) and s[i].isdigit():
                length += s[i]
                i += 1
            i += 1
            length_digit = int(length)
            res.append(s[i:i+length_digit])
            i += length_digit
        return res