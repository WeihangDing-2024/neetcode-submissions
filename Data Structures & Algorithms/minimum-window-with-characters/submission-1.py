class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        unique_char = len(set(t))
        i = 0
        res = float('inf')
        res_s = ""
        for j in range(len(s)):
            curr_char = s[j]
            if curr_char in cnt_t:
                cnt_t[curr_char] -= 1
                if cnt_t[curr_char] == 0:
                    unique_char -= 1
                    while unique_char == 0:
                        if j - i + 1 < res:
                            res = j - i + 1
                            res_s = s[i:j+1]
                        if s[i] in cnt_t:
                            cnt_t[s[i]] += 1
                            if cnt_t[s[i]] > 0:
                                unique_char += 1
                        i += 1
        return res_s
