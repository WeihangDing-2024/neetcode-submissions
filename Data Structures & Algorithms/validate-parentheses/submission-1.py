class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'(': ')', '{': '}', '[': ']'}
        stk = []
        for char in s:
            if char in mp:
                stk.append(char)
            else:
                if (not stk) or char != mp[stk.pop()]:
                    return False
        return not stk
            
        