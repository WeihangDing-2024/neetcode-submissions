class Solution:
    

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "-1"
        seperator = "<43123908>"
        return seperator.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "-1":
            return []
        seperator = "<43123908>"
        return s.split(seperator)