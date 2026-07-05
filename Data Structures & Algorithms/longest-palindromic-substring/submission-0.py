class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 1
        res_idx = [0, 1]

        def helper(i):
            local_res_idx = [i, i+1]
            offset = 1
            while True:
                low, high = i - offset, i + offset
                if low < 0 or high >= len(s):
                    break
                if s[low] != s[high]:
                    break
                local_res_idx = [i-offset, i+offset+1]
                offset += 1
            return local_res_idx

        def even_helper(i, j):
            local_res_idx = [i, j+1]
            offset = 1
            while True:
                low, high = i - offset, j + offset
                if low < 0 or high >= len(s):
                    break
                if s[low] != s[high]:
                    break
                local_res_idx = [i-offset, j+offset+1]
                offset += 1
            return local_res_idx
            
        # odd number palindrom
        for i in range(len(s)):
            temp_idx = helper(i)
            if temp_idx[1] - temp_idx[0] > res:
                res = temp_idx[1] - temp_idx[0]
                res_idx = temp_idx
        
        # even number palindrom
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                temp_idx = even_helper(i, i + 1)
            if temp_idx[1] - temp_idx[0] > res:
                res = temp_idx[1] - temp_idx[0]
                res_idx = temp_idx        
        return s[res_idx[0]:res_idx[1]]

        