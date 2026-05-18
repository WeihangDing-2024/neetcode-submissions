class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        unique_char_remain = len(set(t))

        res = ""
        res_len = float('inf')
        i, j = 0, 0

        while j < len(s):
            char = s[j]
            if char in cnt_t:
                cnt_t[char] -= 1
                if cnt_t[char] == 0:
                    unique_char_remain -= 1

                # move left window to the next 
                if unique_char_remain <= 0:
                    while unique_char_remain <= 0:
                        if s[i] in cnt_t:
                            cnt_t[s[i]] += 1
                            if cnt_t[s[i]] > 0:
                                unique_char_remain += 1
                        i += 1

                    # print(f"{i}, {j}")
                
                    # update res
                    if j - i + 2 < res_len:
                        res_len = j - i + 2
                        res = s[i-1: j+1]
            j += 1
        return res