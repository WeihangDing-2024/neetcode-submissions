class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_lst = []
        for char in s:
            if char.isalpha():
                char_lst.append(char.lower())
        i = 0
        j = len(char_lst) - 1
        while i < j:
            if char_lst[i] != char_lst[j]:
                return False
            i += 1
            j -= 1
        return True
        