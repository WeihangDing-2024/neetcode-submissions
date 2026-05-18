class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapping = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in mapping:
                if not stk:
                    return False
                if stk.pop() != mapping[char]:
                    return False
            else:
                stk.append(char)
        if stk:
            return False
        return True
        
        